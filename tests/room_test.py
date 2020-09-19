import unittest

from src.room import Room
from src.songs import Songs
from src.guests import Guests

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Voodoo", [],[], 10)

    def test_room_has_name(self):
        self.assertEqual("Voodoo", self.room.name)

    def test_room_has_guest_list(self):
        self.assertEqual([], self.room.guest_list)
    
    def test_room_has_song_list(self):
        self.assertEqual([], self.room.song_list)