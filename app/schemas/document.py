from pydantic import BaseModel, Field
from typing import Optional

from app.models.document import DocumentStatus

class DocumentBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=120, description="Document title (3-120 chars)")
    content: Optional[str] = ""


class DocumentCreate(DocumentBase):
    pass 


class DocumentUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=120)
    content: Optional[str] = None


 