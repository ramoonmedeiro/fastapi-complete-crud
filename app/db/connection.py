from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv, find_dotenv
import os
load_dotenv(find_dotenv())

DB_URL = os.getenv("DB_URL")
engine = create_engine(DB_URL, pool_pre_ping=True)
Session = sessionmaker()
