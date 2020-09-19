import unittest

from src.room import Room
from src.songs import Songs
from src.guests import Guests

class TestGuests(unittest.TestCase):
    def setUp(self):
        self.guests = Guests("John", 35, 50)

    def test_guest_has_name(self):
        self.assertEqual("John", self.guests.name)

    def test_guest_has_age(self):
        self.assertEqual(35, self.guests.age)
    
    def test_guest_has_money(self):
        self.assertEqual(50, self.guests.money)
