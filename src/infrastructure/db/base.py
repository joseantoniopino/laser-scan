from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

connection = os.environ.get("DB_CONNECTION")
host = os.environ.get("DB_HOST")
port = os.environ.get("DB_PORT")
database = os.environ.get("DB_DATABASE")
username = os.environ.get("DB_USERNAME")
password = os.environ.get("DB_PASSWORD")

engine = create_engine(f"{connection}://{username}:{password}@{host}:{port}/{database}")
Session = sessionmaker(bind=engine)
