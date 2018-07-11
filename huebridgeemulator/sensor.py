"""Module defining Hue Sensor classes."""

from huebridgeemulator.common import BaseResource


def generate_daylight_sensor():
    """Generate the daylight sensor."""
    data = {
        "config": {
            "configured": False,
            "on": True,
            "sunriseoffset": 30,
            "sunsetoffset": -30},
        "manufacturername": "Philips",
        "modelid": "PHDL00",
        "name": "Daylight",
        "state": {
            "daylight": None,
            "lastupdated": "none"},
        "swversion": "1.0",
        "type": "Daylight"
    }
    return Sensor(data)


class Sensor(BaseResource):
    """Hue Sensor class."""

    _RESOURCE_TYPE = "sensors"
    _MANDATORY_ATTRS = ("config", "manufacturername", "modelid",
                        "name", "state", "swversion", "type")
    _OPTIONAL_ATTRS = ()
    # Should we create SensorState class ???
