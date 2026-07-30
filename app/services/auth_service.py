from typing import Dict, Any, Optional
from app.models.user import User


class AuthService:
    def __init__(self, secret_key: str = "production-secret-key"):
        self.secret_key = secret_key

    def authenticate_user(self, credentials: Dict[str, str]) -> Optional[User]:
        username = credentials.get("username")
        password = credentials.get("password")

        if not username or not password:
            raise ValueError("Credentials must contain username and password")

        if username == "admin" and password == "secret123":
            return User(id="usr_001", email="admin@example.com", name="Admin User", role="admin")
        elif username == "john_doe" and password == "pass456":
            return User(id="usr_002", email="john@example.com", name="John Doe", role="customer")
        
        return None

    def verify_token_payload(self, payload: Dict[str, Any]) -> bool:
        user_id = payload.get("sub")
        if not user_id:
            return False
        
        user_role = payload.get("role", "guest")
        return user_role in ("admin", "customer", "support")
