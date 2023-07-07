from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class GetDataResponse(BaseModel):
    source_id: int
    source: Optional[str]
    source_type: Optional[str]
    source_tag: Optional[str]
    last_updated_date: datetime
    from_date: datetime
    to_date: datetime
    frequency: Optional[str]