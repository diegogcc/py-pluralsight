from unittest.mock import Mock

from alarm import Alarm
from sensor import Sensor


def test_alarm_is_off_by_default():
    alarm = Alarm()
    assert not alarm.is_alarm_on


'''
A Stub has the same methods as the class it replaces, 
but the implementation is very simple
'''
class StubSensor:
    def sample_pressure(self):
        return 15

def test_low_pressure_activates_alarm():
    alarm = Alarm(sensor=StubSensor())
    alarm.check()
    assert alarm.is_alarm_on


'''
Stub sensor created with the Mock framework that comes with the unittest module
I can tell the sensor what to return
'''
def test_normal_pressure_alarm_stays_off():
    stub_sensor = Mock(Sensor)
    stub_sensor.sample_pressure.return_value = 18
    alarm = Alarm(sensor=stub_sensor)
    alarm.check()
    assert not alarm.is_alarm_on  


def test_high_pressure_activates_alarm():
    stub_sensor = Mock(Sensor)
    stub_sensor.sample_pressure.return_value = 22
    alarm = Alarm(sensor=stub_sensor)
    alarm.check()
    assert alarm.is_alarm_on