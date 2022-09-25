import unittest
from classes.guest import Guest
from classes.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        #instantiate guest and song objects 
        self.guest = Guest("Peter", 100.00, "Bohemian rhapsody")
        self.song = Song("Under preassure", "Queen")


    def test_has_name_guest(self):
        expexted = "Peter"
        actual = self.guest.name

    def test_has_cash_guest(self):
        expected = 100.00
        actual = self.guest.cash   

    def test_has_favourite_song_gest(self):
        expected = "Bohemian rhapsody"
        actual = self.guest.favourite_song    

    def test_decrease_cash_guest(self):
        #Act
        self.guest.decrease_cash_guest(self.song.price) 
        #Assert
        expected = 98.00
        actual = self.guest.cash    
        self.assertEqual(expected, actual)

        
        

   