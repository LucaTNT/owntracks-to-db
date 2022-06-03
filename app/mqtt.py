import json
import logging
import paho.mqtt.client as mqtt

class MQTT:
    db = None
    client = None
    DEBUG = False
    config = {
        "mqtt_server": "localhost",
        "mqtt_port": 1883,
        "mqtt_auth": False,
        "mqtt_user": "",
        "mqtt_password": "",
        "mqtt_topic": "owntracks/#"
    }

    def __init__(self, db, config={}) -> None:
        # sourcery skip: default-mutable-arg
        for key, value in config.items():
            if key in self.config:
                self.config[key] = value
            else:
                raise self.UnknownConfigSetting(f"Unknown config key: {key}")       

        self.db = db

        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        if self.config.get("mqtt_auth") == True:
            self.client.username_pw_set(self.config.get("mqtt_user"), password=self.config.get("mqtt_password"))

        try:    
            self.client.connect(self.config.get("mqtt_server"), self.config.get("mqtt_port"), 60)
        except Exception as e:
            logging.error(f"Error connecting to MQTT Server: {e}")
            raise

    def start(self):
        self.client.loop_forever()

    def on_connect(self, client, userdata, flags, rc):
        logging.debug(f"Connected with result code {str(rc)}")

        self.client.subscribe(self.config.get("mqtt_topic"))

    def on_message(self, client, userdata, msg):
        print(f"{msg.topic}: {str(msg.payload)}")
        try:
            data = json.loads(msg.payload)
            if data.get("_type") == "location":
                self.db.add_location(data)
                print("Location added")
        except json.decoder.JSONDecodeError:
            print("Unable to decode JSON")
        except Exception as e:
            print(e)

    class UnknownConfigSetting(Exception):
        def __init__(self, *args: object) -> None:
            super().__init__(*args)
