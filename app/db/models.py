from datetime import datetime

from sqlalchemy import Column, DateTime, String
from sqlalchemy import Integer, ForeignKey
from sqlalchemy import Table
from sqlalchemy.orm import relationship

from .base import Base


class TimeStampedColumns:
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


flow_tags = Table(
    "flow_tags",
    Base.metadata,
    Column("flow_id", Integer, ForeignKey("flows.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id"), primary_key=True),
    Column("created_at", DateTime, default=datetime.utcnow),
    Column("updated_at", DateTime, default=datetime.utcnow, onupdate=datetime.utcnow),
)


class FlowDB(Base):
    __tablename__ = "flows"
    __allow_unmapped__ = True

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, index=True)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    tags = relationship("TagDB", secondary=flow_tags, back_populates="flows")


class TagDB(Base, TimeStampedColumns):
    __tablename__: str = "tags"
    __allow_unmapped__ = True

    id = Column(Integer, primary_key=True, index=True)
    tag_name = Column(String, unique=True, index=True)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    flows = relationship("FlowDB", secondary=flow_tags, back_populates="tags")
