from dataclasses import dataclass
from typing import Optional


@dataclass
class PaymentMethod:
    card_number: str
    exp_month: int
    exp_year: int
    cvv: str
    promo_code: Optional[str] = None


@dataclass
class Transaction:
    transaction_id: str
    order_id: str
    amount: float
    currency: str = "USD"
    status: str = "success"
