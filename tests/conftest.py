"""Shared fixtures for the Rohlik.cz integration tests."""
from __future__ import annotations

import pytest


@pytest.fixture(autouse=True)
def auto_enable_custom_integrations(enable_custom_integrations):
    """Enable loading of the custom integration in every test."""
    yield


@pytest.fixture(autouse=True)
def no_order_item_requests():
    """Stub the upcoming-order item lookup so no test reaches the network.

    Tests that check the item list patch ``OrderService.get_items`` themselves.
    """
    from unittest.mock import AsyncMock, patch

    with patch(
        "rohlik_api.services.orders.OrderService.get_items",
        new=AsyncMock(return_value=[]),
    ):
        yield
