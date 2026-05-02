import traceback
import sys
from database import SessionLocal, engine, Base
import models, auth

# Ensure DB tables exist
Base.metadata.create_all(bind=engine)

payload = {
    "username": "testuser_local_1",
    "email": "test_local_1@example.com",
    "password": "Password123!"
}

db = SessionLocal()
try:
    existing = db.query(models.User).filter(models.User.email == payload["email"]).first()
    print("Existing by email:", bool(existing))

    hashed_pw = auth.hash_password(payload["password"])
    new_user = models.User(
        username=payload["username"],
        email=payload["email"],
        hashed_password=hashed_pw,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    print("Inserted user id:", new_user.id)
except Exception as e:
    print("EXCEPTION:", type(e).__name__, str(e))
    traceback.print_exc()
finally:
    db.close()
