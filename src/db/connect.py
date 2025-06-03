from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

def returnSession():
    USER= os.getenv('DB_USER')
    PASSWORD= os.getenv('DB_PASS')
    HOST= os.getenv('DB_HOST')
    DB= os.getenv('DB_NAME')
    PORT= os.getenv('DB_PORT')

    DATABASE_URL = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}'
    engine = create_engine(DATABASE_URL, echo=True)
    Session = sessionmaker(bind=engine)
    
    return Session()

