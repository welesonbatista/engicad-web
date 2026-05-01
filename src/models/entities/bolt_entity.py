import uuid
from sqlalchemy import Column, String, Float, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from src.core.metadata import Base


class BoltEntity(Base):
    __tablename__ = "bolts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    diameter = Column(Float, nullable=False)
    length = Column(Float, nullable=False)
    head_height = Column(Float, nullable=False)
    head_size = Column(Float, nullable=False)
    hole = Column(Float, nullable=False)
    file_path = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())  # pylint: disable=not-callable
