from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a new database in PostgreSQL db and paste the credentials with db name to be used for database URL
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:root1234@localhost/edge-fastapi"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# to get the db session to be able to perform db operations anywhere in the code
def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.rollback()
    finally:
        db.close()