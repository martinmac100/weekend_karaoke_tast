class Room:
    def __init__(self, room_name, guest_list, song_list, cash_register):
        self.room = room_name
        self.guest_list = []
        self.song_list = []
        self.cash_register = cash_register


    def add_guest_to_room(self, guest):
        # guest = self.room.guest_1
        self.guest_list.append(guest)