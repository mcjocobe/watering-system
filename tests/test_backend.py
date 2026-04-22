import pytest
from watering_system.gateway import set_relay, set_relay_request

def test_set_on():
    print(set_relay_request(target_ip="http://192.168.1.245", state="on"))
