from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from .database import Base


class OCRHistory(Base):
    __tablename__ = "ocr_history"

    id = Column(Integer, primary_key=True, index=True)

    filename = Column(String)

    extracted_text = Column(String)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )