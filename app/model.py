from sqlalchemy import (create_engine, Column, Integer, String,
                        and_, NUMERIC, or_)
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("postgresql://postgres:1@localhost:5432/postgres",
                       echo=True)
Session = sessionmaker(bind=engine, autoflush=False, autocommit=False)
db = Session()
Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    image = Column(String)
    fullname = Column(String, nullable=False)
    job = Column(String)
    about = Column(String)



Base.metadata.create_all(engine)
