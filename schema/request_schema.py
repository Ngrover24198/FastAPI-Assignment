from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class AddDataRequest(BaseModel):
    source_id: int
    source: Optional[str]
    source_type: Optional[str]
    source_tag: Optional[str]
    last_updated_date: Optional[datetime]
    from_date: Optional[datetime]
    to_date: Optional[datetime]
    frequency: Optional[str]
    
class UpdateDataRequest(BaseModel):
    source_id: int
    last_updated_date: Optional[datetime]
    from_date: Optional[datetime]
    to_date: Optional[datetime]
    
class GetDataRequest(BaseModel):
    source_id: int
