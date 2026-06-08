"""
Seed script — creates a default admin user.

Usage:
    python seed.py

Run this once after starting the database.
If the admin email already exists, the script exits safely.
"""

import sys
import os

# Make sure the app package is importable when running from /backend
sys.path.insert(0, os.path.dirname(__file__))

from app.core.database import SessionLocal
from app.core.database import base
from app.core.database import engine
from app.users.models import user_model
from app.utils.hashing import hash_password

# ── Default admin credentials ──────────────────────────────
ADMIN_NAME = "Admin"
ADMIN_EMAIL = "admin@example.com"
ADMIN_PASSWORD = "admin123"
# ───────────────────────────────────────────────────────────


def seed_admin():
    # Ensure tables exist
    base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        existing = db.query(user_model).filter(user_model.email == ADMIN_EMAIL).first()

        if existing:
            print(f"[seed] Admin already exists: {ADMIN_EMAIL}")
            return

        admin = user_model(
            name=ADMIN_NAME,
            email=ADMIN_EMAIL,
            hashed_password=hash_password(ADMIN_PASSWORD),
            role="admin",
        )

        db.add(admin)
        db.commit()

        print("[seed] Admin user created successfully")
        print(f"       Email    : {ADMIN_EMAIL}")
        print(f"       Password : {ADMIN_PASSWORD}")
        print("       Role     : admin")
        print()
        print("[!] Change the password after first login.")

    finally:
        db.close()


if __name__ == "__main__":
    seed_admin()
