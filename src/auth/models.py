import datetime

from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy import (JSON, TIMESTAMP, Boolean, Column, ForeignKey, Integer,
                        MetaData, String, Table)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


metadata = MetaData() # для миграций


role = Table(
    'role',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('permissions', JSON)
    
)

user = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('email', String, nullable=False),
    Column('username', String, nullable=False),
    Column('registred_at', TIMESTAMP, default=datetime.datetime.now),
    Column('role_id', Integer, ForeignKey(role.c.id)),
    Column('hashed_password', String, nullable=False),
    Column('is_active', Boolean, default=True, nullable=False),
    Column('is_superuser',Boolean, default=False, nullable=False),
    Column('is_verified', Boolean, default=False, nullable=False))



class Base(DeclarativeBase):
    pass



class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    registred_at = Column(TIMESTAMP, default=datetime.datetime.now)
    role_id = Column(Integer, ForeignKey(role.c.id))
    hashed_password:str = Column(String(length=1024), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)