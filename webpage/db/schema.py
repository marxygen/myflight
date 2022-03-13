from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Float, String, DateTime

Base = declarative_base()


class Flight(Base):
    __tablename__ = 'flights'

    code = Column(String(10), primary_key=True)
    reg_number = Column(String(20))
    flag = Column(String(3))
    lat = Column(Float(6))
    lng = Column(Float(6))
    alt = Column(Float(6))
    speed = Column(Float(3))
    v_speed = Column(Float(3))
    dep_iata = Column(String(20))
    arr_iata = Column(String(20))
    dep_gate = Column(String(20))
    dep_time_utc = Column(DateTime(timezone=True), nullable=True)
    arr_time_utc = Column(DateTime(timezone=True), nullable=True)
    model = Column(String(20))
    delayed = Column(String(20))
    status = Column(String(10))

    def __repr__(self):
        return f'[{self.code}] {self.aircraft_icao} (from {self.dep_iata} to {self.arr_iata}, {self.status})'
