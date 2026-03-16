import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    postgres_user: str = "postgres"
    postgres_password: str = "password"
    postgres_db: str = "mydb"
    db_host: str = "db"
    db_port: str = "5432"

    @property
    def database_url(self):
        return f"postgresql://{self.postgres_user}:{self.postgres_password}@{self.db_host}:{self.db_port}/{self.postgres_db}"

settings = Settings()

engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency to get a DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
