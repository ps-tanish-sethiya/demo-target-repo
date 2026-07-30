from typing import List, Optional
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class OrderItem:
    item_id: str
    title: str
    unit_price: float
    quantity: int

    @property
    def total_price(self) -> float:
        return self.unit_price * self.quantity


@dataclass
class ShippingAddress:
    street: str
    city: str
    state: str
    zip_code: str
    country: str = "US"


@dataclass
class Order:
    order_id: str
    user_id: str
    items: List[OrderItem]
    status: str = "pending"
    shipping_address: Optional[ShippingAddress] = None
    created_at: datetime = field(default_factory=datetime.utcnow)

    @property
    def subtotal(self) -> float:
        return sum(item.total_price for item in self.items)
