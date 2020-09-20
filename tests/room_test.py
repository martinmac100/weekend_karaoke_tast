import unittest

from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        
        self.room = Room("Voodoo", [],[], 10)
        
        self.song_1 = Song("Babies", "Pulp")
        self.song_2 = Song("As", "Stevie Wonder")
        self.song_3 = Song ("Raspberry Beret", "Prince")
        
        self.room.song = [self.song_1, self.song_2, self.song_3]

        self.guest_1 = Guest("John", 35, 50)
        self.guest_2 = Guest("Paul", 40, 300)
        self.guest_3 = Guest("George", 45, 10)
        self.guest_4 = Guest("Ringo", 17, 30)

    def test_room_has_name(self):
        self.assertEqual("Voodoo", self.room.room_name)

    def test_room_has_guest_list(self):
        self.assertEqual([], self.room.guest_list)
    
    def test_room_has_song_list(self):
        self.assertEqual([], self.room.song_list)
    
    def test_add_guest_to_room(self):
        self.room.add_guest_to_room(self.guest_1)
        self.assertEqual([self.guest_1],self.room.guest_list)

    # def test_remove_guest_from_room(self):
    #     self.room.remove_guest_from_room(self.guest_1)
    #     self.assertEqual([None],self.room.guest_list)

    def test_add_song_title_to_room(self):
        self.room.add_song_title_to_room(self.song_1)
        self.assertEqual([self.song_1],self.room.song_list)
