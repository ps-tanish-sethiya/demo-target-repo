"""
Automated Test Suite for E-Commerce Backend Microservices.
"""

import pytest
from app.models.user import User
from app.models.order import Order, OrderItem, ShippingAddress
from app.services.auth_service import AuthService
from app.services.payment_service import PaymentProcessor
from app.services.order_service import OrderService


def test_user_authentication():
    auth = AuthService()
    user = auth.authenticate_user({"username": "john_doe", "password": "pass456"})
    assert user is not None
    assert user.email == "john@example.com"
    assert user.role == "customer"


def test_token_payload_verification():
    auth = AuthService()
    payload = {"sub": "usr_999", "role": "customer"}
    assert auth.verify_token_payload(payload) is True


def test_payment_calculation():
    processor = PaymentProcessor()
    order = Order(
        order_id="ord_101",
        user_id="usr_002",
        items=[
            OrderItem(item_id="it_1", title="Wireless Mouse", unit_price=25.00, quantity=2),
            OrderItem(item_id="it_2", title="Mechanical Keyboard", unit_price=100.00, quantity=1)
        ]
    )
    result = processor.process_payment(order, {"card_number": "4111111111111111", "promo_code": "SAVE20"})
    assert result["success"] is True
    assert result["charged_amount"] == 120.00


def test_shipping_label_formatting():
    service = OrderService()
    
    # Guest checkout order created without explicit shipping address
    order = Order(
        order_id="ord_102",
        user_id="usr_guest",
        items=[OrderItem(item_id="it_3", title="USB-C Cable", unit_price=15.00, quantity=1)],
        shipping_address=None
    )
    
    label = service.format_shipping_label(order)
    assert "Order #ord_102" in label

def test_vip_discount():
    processor = PaymentProcessor()
    order = Order(
        order_id="ord_999",
        user_id="usr_vip",
        items=[OrderItem(item_id="it_1", title="Laptop", unit_price=1000.00, quantity=1)]
    )
    result = processor.process_payment(order, {"card_number": "4111111111111111", "promo_code": "VIP50"})
    assert result["charged_amount"] == 500.00
