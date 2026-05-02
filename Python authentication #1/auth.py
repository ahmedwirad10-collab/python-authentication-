from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"

# NOTE:
# Your current environment has a broken `bcrypt` backend (passlib raises:
# "module 'bcrypt' has no attribute '__about__'"), which causes /register to 500.
# Switching to pbkdf2_sha256 fixes hashing so the API can work.
pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

# Hash password
def hash_password(password: str):
    return pwd_context.hash(password)

# Verify password
def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

# Create JWT token
def create_access_token(data: dict, expires_minutes: int = 30):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_minutes)
    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
