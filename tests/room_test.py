import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(5.00, 20)
        self.guest = Guest("Peter", 100.00, "Bohemian rhapsody")
        self.song = Song("Bohemian rhapsody", "Queen")

    def test_has_entry_fee(self):
        expected = 5.00
        actual = self.room.entry_fee
        self.assertEqual(expected, actual)   

    def test_has_capacity_room(self):
        expected = 20 
        actual = self.room.capacity_room
        self.assertEqual(expected, actual)

    def test_check_in_guest(self):
        #Act
        result = self.room.check_in_guest(self.guest)
        #Assert
        expected = self.guest
        actual = result
        self.assertEqual(expected, actual)

    def test_check_out_guest(self):
        #Act --- check in guest to room
        result = self.room.check_in_guest(self.guest)
        #Assert
        expected = self.guest
        actual = result
        self.assertEqual(expected, actual)
            

    def test_find_song_by_name(self):
         #Act 
         self.room.add_song_to_room(self.song)
         #Assert
         expect = "Bohemian rhapsody"
         actual = self.room.find_song_by_name(self.song.title)
         self.assertEqual(expect, actual)
             

    def test_add_song_to_room(self):
        #Act
        self.room.add_song_to_room(self.song)
        #Assert
        expected = "Bohemian rhapsody"
        actual = self.room.find_song_by_name(self.song.title)
        self.assertEqual(expected, actual)

    def test_more_check_in(self):
        #Act -- we have 20 available spaces, so we need 21 new instances checked in make test fail
        #just check in one
        self.room.check_in_guest(self.guest)
     
        expexted = True
        actual = self.room.more_guest_check_in()
        self.assertEqual(expexted, actual)

    def test_pay_entry_fee(self):
        expected = True
        actual = self.room.pay_entry_fee(self.guest)
        self.assertEqual(expected, actual)   

    def test_guest_favourite_song(self):
        #Act - add song to room and check in guest as well
        self.room.add_song_to_room(self.song)
        result = self.room.check_in_guest(self.guest)
        #print(result)
        #Assert
        #we expect list with one guest object which been checked in
        expected = [result]
        actual = self.room.guest_favourite_song()  
        self.assertEqual(expected, actual)

 

  
        











  
        


