from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Location = declarative_base()

class Location(Location):
    __tablename__ = "locations"
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=datetime.utcnow)
    lat = Column(Float)
    lon = Column(Float)
    alt = Column(Integer)
    SSID = Column(String(128))
    battery = Column(Integer)
    connection_type = Column(String(1))

    def __repr__(self):
        return f"Date(id={self.date!r}: lat={self.lat!r}, lon={self.lon!r}"

