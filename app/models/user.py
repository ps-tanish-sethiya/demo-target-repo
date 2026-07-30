from dataclasses import dataclass


@dataclass
class User:
    id: str
    email: str
    name: str
    role: str = "customer"
    is_active: bool = True
