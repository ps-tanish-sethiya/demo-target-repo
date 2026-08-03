from typing import Dict, Any
from app.models.order import Order


class OrderService:
    def __init__(self):
        self.orders_db: Dict[str, Order] = {}

    def format_shipping_label(self, order: Order) -> str:
        """
        Generates formatted shipping label string for fulfillment warehouse dispatch.
        """
        if not order or not getattr(order, "shipping_address", None):
            order_id = getattr(order, "order_id", "UNKNOWN") if order else "UNKNOWN"
            return f"RECIPIENT: Order #{order_id}\nLOCATION: Digital Delivery / Guest Checkout"

        addr = order.shipping_address
        
        # 🛡️ Bulletproof Fallbacks: Handle missing city/country/street/state/zip
        city = getattr(addr, "city", None) or "UNKNOWN CITY"
        country = getattr(addr, "country", None) or "UNKNOWN COUNTRY"
        street = getattr(addr, "street", None) or "N/A"
        state = getattr(addr, "state", None) or "N/A"
        zip_code = getattr(addr, "zip_code", None) or "N/A"

        return (
            f"RECIPIENT: Order #{order.order_id}\n"
            f"STREET: {street}\n"
            f"LOCATION: {city.upper()}, {state} {zip_code}\n"
            f"COUNTRY: {country.upper()}"
        )
