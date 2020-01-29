import datetime
import itertools
import random
import time

class Sensor:
    def __iter__(self):
        return self

    def __next__(self):
        return random.random()

sensor = Sensor()
timestamp = iter(datetime.datetime.now, None)

for stamp, value in itertools.islice(zip(timestamp, sensor), 10):
    print(stamp, value)
    time.sleep(1)


'''
In python's terminal:

>>> import sensor
2020-01-28 20:03:32.240765 0.5682683406107564
2020-01-28 20:03:33.245004 0.7841956853780012
2020-01-28 20:03:34.245200 0.5188386467587061
2020-01-28 20:03:35.247417 0.9397653068530567
2020-01-28 20:03:36.251680 0.4448028181780379
2020-01-28 20:03:37.256661 0.36704629564112834
...
...

'''