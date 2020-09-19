import unittest

from src.room import Room
from src.song import Song
from src.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("John", 35, 50)

    def test_guest_has_name(self):
        self.assertEqual("John", self.guest.name)

    def test_guest_has_age(self):
        self.assertEqual(35, self.guest.age)
    
    def test_guest_has_money(self):
        self.assertEqual(50, self.guest.money)
