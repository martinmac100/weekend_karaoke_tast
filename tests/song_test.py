import unittest

from src.room import Room
from src.song import Song
from src.guest import Guest

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_3 = Song ("Raspberry Beret", "Prince")

    def test_song_has_name(self):
        self.assertEqual("Prince", self.song_3.artist)

    def test_song_has_artist(self):
        self.assertEqual("Raspberry Beret", self.song_3.title)

    