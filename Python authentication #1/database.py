from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


engine = create_engine("sqlite:///./auth.db")

SessionLocal = sessionmaker(bind=engine)

DATABASE_URL = "sqlite:///./auth.db"  # you can change to MySQL later

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()