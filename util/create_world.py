from django.contrib.auth.models import User
from adventure.models import Player, Room
import random

Room.objects.all().delete()

room_count = 0
rooms = []
dirs = {0: 'n', 1: 's', 2: 'e', 3: 'w'}
reverse_dirs = {0: 's', 1: 'n', 2: 'w', 3: 'e'}
num_rooms = 500

while room_count < num_rooms:
    if room_count is 0:
        room = Room(title = "A Generic Room", description = "This is a generic room.")
        rooms.append(room)
        room_count += 1
    rand_room = rooms[random.randint(0, len(rooms) - 1)]
    dir = random.randint(0, 3)
    rand_dir = dirs[dir]
    rev_dir = reverse_dirs[dir]
    if rand_dir is 'n':
        if rand_room.n_to is 0:
            new_room = Room(title = "A Generic Room",
                            description = "This is a generic room.")
            new_room.save()
            rand_room.connectRooms(new_room, rand_dir)
            new_room.connectRooms(rand_room, rev_dir)
            new_room.save()
            rooms.append(new_room)
            room_count += 1
    elif rand_dir is 's':
        if rand_room.s_to is 0:
            new_room = Room(title = "A Generic Room",
                            description = "This is a generic room.")
            new_room.save()
            rand_room.connectRooms(new_room, rand_dir)
            new_room.connectRooms(rand_room, rev_dir)
            new_room.save()
            rooms.append(new_room)
            room_count += 1
    elif rand_dir is 'e':
        if rand_room.e_to is 0:
            new_room = Room(title = "A Generic Room",
                            description = "This is a generic room.")
            new_room.save()
            rand_room.connectRooms(new_room, rand_dir)
            new_room.connectRooms(rand_room, rev_dir)
            new_room.save()
            rooms.append(new_room)
            room_count += 1
    elif rand_dir is 'w':
        if rand_room.w_to is 0:
            new_room = Room(title = "A Generic Room",
                            description = "This is a generic room.")
            new_room.save()
            rand_room.connectRooms(new_room, rand_dir)
            new_room.connectRooms(rand_room, rev_dir)
            new_room.save()
            rooms.append(new_room)
            room_count += 1
    rand_room.save()

"""for room in rooms:
    room.save()"""

players = Player.objects.all()
for p in players:
    p.currentRoom = rooms[0].id
    p.save()
