class Room:
    def __init__(self, entry_fee, capacity_room):
        self.guest_list = []
        self.song_list = []
        self.entry_fee = entry_fee
        self.capacity_room = capacity_room
        
        
        
       
        

    def check_in_guest(self, guest):
        
           self.guest_list.append(guest)
           return guest
        
       
        
    def check_out_guest(self, guest_name):
       # if len(self.guest_list) != 0:
            for guest in self.guest_list:
                if guest.name == guest_name:
                    self.guest_list.remove(guest)
          

    def add_song_to_room(self, song):
        self.song_list.append(song) 

    def find_song_by_name(self, title):
        for song in self.song_list:
            if song.title == title:
                return song.title 

    def add_song_to_room(self, song):
        self.song_list.append(song)   

    def more_guest_check_in(self):
        is_available_space = False
        if len(self.guest_list) < self.capacity_room:
            is_available_space = True
        return is_available_space   

    def pay_entry_fee(self, guest):
        is_cash_enough = False
        if guest.cash >= self.entry_fee:
            is_cash_enough = True     
        return is_cash_enough

    def guest_favourite_song(self):
        whoo_list = []
        for guest in self.guest_list:
            #found fav song for each guest and add into the llist
            for song in self.song_list:
                if song.title == guest.favourite_song:
                    whoo_list.append(guest)
        return whoo_list
         
        


         



   