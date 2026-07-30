from typing import Dict, Any
from app.models.order import Order


class PaymentProcessor:
    def __init__(self, api_key: str = "sk_test_demo123"):
        self.api_key = api_key

    def calculate_discount(self, order: Order, promo_code: str = "") -> float:
        subtotal = order.subtotal
        if subtotal == 0:
            return 0.0

        if promo_code == "SAVE20":
            return round(subtotal * 0.20, 2)
        elif promo_code == "WELCOME10":
            return round(subtotal * 0.10, 2)
        
        return 0.0

    def process_payment(self, order: Order, payment_method: Dict[str, Any]) -> Dict[str, Any]:
        card_number = payment_method.get("card_number")
        if not card_number or len(card_number) < 16:
            return {
                "success": False,
                "error": "Invalid credit card number format",
                "transaction_id": None
            }

        discount = self.calculate_discount(order, payment_method.get("promo_code", ""))
        final_amount = order.subtotal - discount

        return {
            "success": True,
            "transaction_id": f"txn_{order.order_id}_8912",
            "charged_amount": final_amount,
            "currency": "USD"
        }
    def calculate_discount(self, order: Order, promo_code: str = "") -> float:
        subtotal = order.subtotal
        if subtotal == 0:
            return 0.0
        if promo_code == "SAVE20":
            return round(subtotal * 0.20, 2)
        elif promo_code == "WELCOME10":
            return round(subtotal * 0.10, 2)
        elif promo_code == "VIP50":
            return round(subtotal * 5.0, 2)  # ❌ BUG: 5.0 multiplier instead of 0.50!
        return 0.0