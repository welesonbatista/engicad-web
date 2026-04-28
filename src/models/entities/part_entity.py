import uuid
from sqlalchemy import Column, String, Float
from src.core.metadata import Base

class PartEntity(Base):
    __tablename__ = "parts"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    diameter = Column(Float, nullable=False)
    length = Column(Float, nullable=False)
    hole_diameter = Column(Float, nullable=False)
    file_path = Column(String, nullable=False)