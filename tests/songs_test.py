import unittest

from src.room import Room
from src.songs import Songs
from src.guests import Guests

class TestSongs(unittest.TestCase):
    def setUp(self):
        self.songs = Songs ("Raspberry Beret", "Prince")

    def test_song_has_name(self):
        self.assertEqual("Prince", self.songs.artist)

    def test_song_has_artist(self):
        self.assertEqual("Raspberry Beret", self.songs.title)

    