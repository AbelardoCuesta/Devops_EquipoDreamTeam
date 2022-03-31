from sqlalchemy import Column, String, Float
from .base import Base
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from datetime import timedelta
from datetime import datetime
from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.sql import func
from utils.crypto import uuid4Str

# Modelo para la entidad Producto
class Lista_negra(Base):
    __tablename__ = "lista_negra"

    id = Column(String(40), primary_key=True, default=uuid4Str)
    email = Column(String(100), nullable=False)
    app_uuid = Column(String(100), nullable=False)
    blocked_reason = Column(String(256), nullable=False)
    ip = Column(String(100), nullable=False)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    

lista_negra_parser = sqlalchemy_to_pydantic(Lista_negra)