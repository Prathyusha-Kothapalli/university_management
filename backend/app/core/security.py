import bcrypt
import os
import time
from typing import Optional, Dict, Any
import jwt

SECRET_KEY = os.getenv("JWT_SECRET_KEY", "unisphere-enterprise-super-secret-jwt-key-2026")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24  # 24 hours
REFRESH_TOKEN_EXPIRE_DAYS = 30

# RBAC Bitmasks for Enterprise Roles
PERMISSION_READ_STUDENTS = 1 << 0      # 1
PERMISSION_WRITE_STUDENTS = 1 << 1     # 2
PERMISSION_MANAGE_FACULTY = 1 << 2     # 4
PERMISSION_PUBLISH_GRADES = 1 << 3     # 8
PERMISSION_MANAGE_FINANCE = 1 << 4     # 16
PERMISSION_SYSTEM_ADMIN = 1 << 5       # 32

ROLE_PERMISSIONS = {
    "admin": 0xFFFFFFFF,
    "hod": PERMISSION_READ_STUDENTS | PERMISSION_WRITE_STUDENTS | PERMISSION_MANAGE_FACULTY | PERMISSION_PUBLISH_GRADES,
    "faculty": PERMISSION_READ_STUDENTS | PERMISSION_WRITE_STUDENTS | PERMISSION_PUBLISH_GRADES,
    "student": PERMISSION_READ_STUDENTS,
    "parent": PERMISSION_READ_STUDENTS,
    "librarian": PERMISSION_READ_STUDENTS | PERMISSION_WRITE_STUDENTS,
}


def get_password_hash(password: str) -> str:
    password_bytes = password.encode("utf-8")

    if len(password_bytes) > 72:
        raise ValueError("Password cannot be longer than 72 bytes.")

    hashed = bcrypt.hashpw(
        password_bytes,
        bcrypt.gensalt()
    )

    return hashed.decode("utf-8")


def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:
    password_bytes = plain_password.encode("utf-8")
    hashed_bytes = hashed_password.encode("utf-8")

    return bcrypt.checkpw(
        password_bytes,
        hashed_bytes
    )


def create_access_token(data: dict, expires_delta: Optional[int] = None) -> str:
    to_encode = data.copy()
    now = int(time.time())
    expire = now + (expires_delta if expires_delta else ACCESS_TOKEN_EXPIRE_MINUTES * 60)
    to_encode.update({"iat": now, "exp": expire, "type": "access"})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def create_refresh_token(data: dict, expires_delta: Optional[int] = None) -> str:
    to_encode = data.copy()
    now = int(time.time())
    expire = now + (expires_delta if expires_delta else REFRESH_TOKEN_EXPIRE_DAYS * 86400)
    to_encode.update({"iat": now, "exp": expire, "type": "refresh"})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token: str) -> Dict[str, Any]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise ValueError("Token has expired")
    except jwt.InvalidTokenError:
        raise ValueError("Invalid token")


def check_permission(user_role: str, required_permission: int) -> bool:
    role_mask = ROLE_PERMISSIONS.get(user_role.lower(), 0)
    return (role_mask & required_permission) == required_permission