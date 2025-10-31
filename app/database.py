from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# postgresql://username:password@host:port/database_name
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1@localhost:5432/shox"
# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()
# db = SessionLocal()
#
#
# def get_db():
#     global db
#     try:
#         return db
#     finally:
#         db.close()


# SQLite3 ------------------------------------------------------------

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
#
# # SQLite uchun connection URL (fayl orqali)
SQLALCHEMY_DATABASE_URL = "sqlite:///./shox.db"

# SQLite da bir nechta threadlar ishlaganda xatolik chiqmasligi uchun `check_same_thread=False`
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()
