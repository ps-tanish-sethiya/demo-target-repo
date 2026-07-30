from typing import Dict, Any
from app.models.order import Order


class OrderService:
    def __init__(self):
        self.orders_db: Dict[str, Order] = {}

    def format_shipping_label(self, order: Order) -> str:
        """
        Generates formatted shipping label string for fulfillment warehouse dispatch.
        """
        addr = order.shipping_address
        city_upper = addr.city.upper()
        country = addr.country.upper()

        return (
            f"RECIPIENT: Order #{order.order_id}\n"
            f"STREET: {addr.street}\n"
            f"LOCATION: {city_upper}, {addr.state} {addr.zip_code}\n"
            f"COUNTRY: {country}"
        )
