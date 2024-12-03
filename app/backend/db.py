from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


engine = create_engine('sqlite:///ecommerce.db', echo=True)
SessionLocal = sessionmaker(bind=engine)

#for postgres
#engine = create_engine('postgresql+psycopg2://youuser:youpassword@localhost/youdb')
#format
#Dialect+driver://username:password@host:port/database

#CREATE MODEL FOR SQLALCHEMY
class Base(DeclarativeBase):  # New
    pass