from os import environ
import logging

from db import DB
from mqtt import MQTT

loglevel = logging.DEBUG if bool(environ.get('DEBUG', 0)) else logging.WARN
logging.basicConfig(level=loglevel)

DB_CONNECTION = environ.get("DB_CONNECTION", "sqlite:///locations.db")

mqtt_config = {}
if MQTT_SERVER := environ.get("MQTT_SERVER"):
    mqtt_config["mqtt_server"] = MQTT_SERVER

if MQTT_PORT := environ.get("MQTT_PORT"):
    mqtt_config["mqtt_port"] = int(MQTT_PORT)\

if MQTT_AUTH := bool(int(environ.get("MQTT_AUTH", 0))):
    mqtt_config["mqtt_auth"] = MQTT_AUTH

if MQTT_USER := environ.get("MQTT_USER"):
    mqtt_config["mqtt_user"] = MQTT_USER

if MQTT_PASSWORD := environ.get("MQTT_PASSWORD"):
    mqtt_config["mqtt_password"] = MQTT_PASSWORD

if MQTT_TOPIC := environ.get("MQTT_TOPIC"):
    mqtt_config["mqtt_topic"] = MQTT_TOPIC

db = DB(DB_CONNECTION)
mqtt = MQTT(db, mqtt_config)
mqtt.start()
