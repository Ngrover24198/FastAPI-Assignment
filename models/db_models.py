from datetime import datetime
from config.db_config import Base
from sqlalchemy import Integer, String
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.schema import Column, ForeignKey, Table
from sqlalchemy.sql.sqltypes import DateTime, Enum
from config.db_config import Base

class Assignment(Base):
    """Base db variable used to create the sample table, according to the description given"""
    __tablename__ = "assignment"
    
    source_id = Column(Integer, primary_key=True, nullable=False)
    source = Column(String(200), nullable=True)
    source_type = Column(String(10), nullable=True)
    source_tag = Column(String(10), nullable=True)
    last_updated_date = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=True)
    from_date = Column(DateTime, default=datetime.now, nullable=True)
    to_date = Column(DateTime, default=datetime.now, nullable=True)
    frequency = Column(String(5), nullable=True)
    
    