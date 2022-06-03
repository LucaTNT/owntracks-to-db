This thing is supposed connect to MQTT and store the data it gets from the [OwnTracks app](https://owntracks.org/) into a database. Might be useful in conjunction with Grafana to create nice-looking dashboards containing long-term location data.

## Usage
Settings are provided through environment variables:

| **Variable**  | **Required** | **Default**              | **Meaning**                                                          |
|---------------|--------------|--------------------------|----------------------------------------------------------------------|
| DB_CONNECTION | No           | `sqlite:///locations.db` | The SQLAlchemy DB connection string.                                 |
| MQTT_SERVER   | No           | `localhost`              |                                                                      |
| MQTT_PORT     | No           | `1883`                   |                                                                      |
| MQTT_AUTH     | No           | `0`                      | Set to `1` to enable MQTT username and password auth.                |
| MQTT_USER     | No           |                          | MQTT username. Only used if `MQTT_AUTH` is set to `1`.               |
| MQTT_PASSWORD | No           |                          | MQTT password. Only used if `MQTT_AUTH` is set to `1`.               |
| MQTT_TOPIC    | No           | `owntracks/#`            | The topic to listen on. Check OwnTracks documentation for more info. |
| DEBUG         | No           |                          | Set to `1` to enable debug output.                                   |

## Limitations
For the time being it only supports a single device being tracked.

## Docker image
A Docker image is provided, it can be used by running, for example:

    docker run -e MQTT_SERVER=mosquitto lucatnt/owntracks-to-db

Configuration is done through the environment variables listed above.
