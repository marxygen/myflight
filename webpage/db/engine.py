from sqlalchemy import create_engine, select
import os
from sqlalchemy.orm import Session
from .schema import Base, Flight


POSTGRES_USER = os.getenv('POSTGRES_USER')
DATABASE_PASSWORD = os.getenv('POSTGRES_PASSWORD')

engine = create_engine(
    f"postgresql://{POSTGRES_USER}:{DATABASE_PASSWORD}@postgis:5432/myflight",
    future=True)


def create_tables():
    Base.metadata.create_all(engine)


def create_flight(**kwargs):
    kwargs = {
        key: value for key,
        value in kwargs.items() if key in Flight.__dict__}
    with Session(engine) as session:
        flight = Flight(
            **kwargs
        )
        session.add(flight)
        session.commit()


def get_flights():
    with Session(engine) as session:
        return list(session.scalars(select(Flight)))


def get_flight(code: str):
    with Session(engine) as session:
        return list(session.scalars(select(Flight).where(Flight.code == code)))
