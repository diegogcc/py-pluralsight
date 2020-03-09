'''
1. UNDERSTAND WHAT TO BUILD
unittests (if well done), can show business decisions and the development applied.

For example:
    Trying to book more seats that the ones that are available
    returns an empty dict.
    It could have raised an exception alternatively.

2. DOCUMENTING THE UNITS
    unit tests specify the behavior of the unit under test
    (methods, how to call them and their results)

    give demonstration on how the developer intender the unit to be used

3. DESIGN THE UNITS
    In order to have unit tests, the code has to have units. 
    Unit tests exercise the interface (function name, parameter list, return type) 
        besides the implementation.

4. DETECT REGRESSIONS
    Something that used to work, no longer does.
'''

import unittest
from theatre import SeatFinder 

# Note: A is the front row, so A6 is the 6th seat on the front row

class SeatFinderTest(unittest.TestCase):

    def test_prefer_near_the_front(self):
        finder = SeatFinder(available_seats={"A6", "B6", "C7"})
        seats = finder.find_seats(1)
        assert seats == {"A6"}

    def test_finds_adjacent_seats_when_more_than_one_requested(self):
        finder = SeatFinder(available_seats={"A6", "A8", "C6", "C7"})
        seats = finder.find_seats(2)
        assert seats == {"C6", "C7"}

    def test_finds_separate_seats_when_adjacent_not_available(self):
        finder = SeatFinder(available_seats={"A6", "B6", "C7"})
        seats = finder.find_seats(2)
        assert seats == {"B6", "A6"}

    def test_find_seats_fails_when_not_enough_available(self):
        finder = SeatFinder(available_seats={"A6", "B6", "C7"})
        seats = finder.find_seats(5)
        assert seats == {}

    '''
    unit tests document design decisions
    like how to book a seat for wheelchair users
    '''
    def test_find_seats_for_wheelchair_users(self):
        finder = SeatFinder(available_seats={"A1W", "A6", "B6", "C7"})
        seats = finder.find_seats(1, wheelchair_count=1)
        assert seats == {"A1W"}