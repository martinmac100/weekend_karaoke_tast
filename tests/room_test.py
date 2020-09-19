import unittest

from src.room import Room
from src.songs import Songs
from src.guests import Guests

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Voodoo", [],[], 10)
        # self.songs_1 = Songs["Babies", "Pulp"]
        self.songs_2 = Songs("As", "Stevie Wonder")
        self.room.songs = [self.songs_1, self.songs_2]

    def test_room_has_name(self):
        self.assertEqual("Voodoo", self.room.title)

    def test_room_has_guest_list(self):
        self.assertEqual([], self.room.guest_list)
    
    def test_room_has_song_list(self):
        self.assertEqual([], self.room.song_list)
    
    def test_add_song_to_room(self):
        song_to_add = self.songs_1.name
        self.assertEqual(3, len(self.songs.title))