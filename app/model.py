# # app/model.py
# import os
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base
#
# DATABASE_URL = os.getenv("DATABASE_URL") or "sqlite:////home/PortfolioMe/portfolio/data.db"
#
# # SQLite bo'lsa, connect_args kerak bo'ladi
# connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
#
# engine = create_engine(DATABASE_URL, pool_pre_ping=True, connect_args=connect_args)
# SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
# Base = declarative_base()
#
# # ⚠️ MUHIM: BU YERDAN create_all() ni olib tashlang!
# # Base.metadata.create_all(engine)  # <-- O'CHIRING
