import unittest

from src.room import Room
from src.songs import Songs
from src.guests import Guests

class TestSongs(unittest.TestCase):
    def setUp(self):
        self.songs = Songs