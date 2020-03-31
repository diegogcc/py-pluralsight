'''
MonkeyPatching:
    Change a piece of code AT RUNTIME.

    A way to insert a test double.

'''

from unittest.mock import patch
from unittest.mock import Mock

from alarm import Alarm


''' In a context manager '''
# We use a monkey patch to replace the sensor with a stub class
def test_alarm_with_high_pressure_value():
    with patch('alarm.Sensor') as test_sensor_class:
        # we use which module should get a reference to the test double,
        # not which module the class is actually declared in
        test_sensor_instance = Mock()
        test_sensor_instance.sample_pressure.return_value = 22  # Monkey patching
        test_sensor_class.return_value = test_sensor_instance

        alarm = Alarm()
        alarm.check()

        assert alarm.is_alarm_on

''' In a decorator '''
@patch('alarm.Sensor')
def test_alarm_with_too_low_pressure_value(test_sensor_class):
    test_sensor_instance = Mock()
    test_sensor_instance.sample_pressure.return_value = 16
    test_sensor_class.return_value = test_sensor_instance

    alarm = Alarm()
    alarm.check()
    
    assert alarm.is_alarm_on