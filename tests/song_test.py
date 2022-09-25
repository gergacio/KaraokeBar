import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    #Arrange/Act/Assert
    #arrange env in special func setUp
    def setUp(self):
        #instantiate object from class Song,invoke Song() invoke __init__ under the hood
        self.song = Song("Under preassure", "Queen")

    #write tests :)
    def test_has_song_title(self):
        expected = "Under preassure"
        actual = self.song.title
        self.assertEqual(expected, actual)

    def test_has_song_artist(self):
        expected = "Queen"
        actual = self.song.artist
        self.assertEqual(expected, actual)  

    def test_song_price(self):
        expected = 2.00
        actual = self.song.price    

        
        


      

    