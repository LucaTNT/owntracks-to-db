from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from datetime import datetime
import logging

from model import Location

class DB:
    engine = None

    def __init__(self, db_connection="sqlite:///locations.db") -> None:
        self.engine = create_engine(db_connection, future=True)
        logging.basicConfig()
        logging.getLogger("sqlalchemy.engine").setLevel(logging.root.level)
        Location.metadata.create_all(self.engine)

    def add_location(self, data) -> Location:
        with Session(self.engine) as session:
            if data.get("lat") and data.get("lon") and data.get("tst"):
                new_location = Location(
                    date = datetime.fromtimestamp(data.get("tst", 0)),
                    lat = data.get("lat"),
                    lon = data.get("lon"),
                    alt = data.get("alt"),
                    SSID = data.get("SSID"),
                    battery = data.get("batt"),
                    connection_type = data.get("conn"),
                )

                session.add(new_location)
                session.commit()
                return new_location
            raise self.IncompleteLocationData("Incomplete location data received")

    class IncompleteLocationData(Exception):
        def __init__(self, *args: object) -> None:
            super().__init__(*args)
