from django.contrib.auth.models import User
from adventure.models import Player, Room
import random

Room.objects.all().delete()

room_count = 0
rooms = []
dirs = {0: 'n', 1: 's', 2: 'e', 3: 'w'}
reverse_dirs = {0: 's', 1: 'n', 2: 'w', 3: 'e'}
num_rooms = 500

names_descriptions = {
    'Treasure Room': 'A room brimming with gold and other treasures.',
    'Hallway': 'This wide hallway leads to other rooms.',
    'Cave': 'A large cave that twists in a maze-like fashion, you can hear water running thoughout.',
    'Bossroom': '',
    'Foyer': 'A spacious room that leads into other rooms',
    'Cliff': 'This room opens up to a cliff overlooking a small inlet, you feel a breeze from the north...',
    'Dragons Nest': 'A small room filled with Dragon eggs, one of them appears cracked...',
    'Narrow Passage': 'As you shimmey through this small corridor, you see light ahead...',
    'Infirmary': 'Heal your injuries here...',
    'Battlement': '',
    'Pantry': '',
    'Library': '',
    'Dungeon': '',
    'Artifact Room': '',
    'Potions Room': '',
    'Summoning Room': '',
    'Workshop': '',
    'Trading Post': '',
    'Hound Room': 'You hear barking in the distance. The bones on the ground don\'t look like dog treats',
    'Forge': '',
    'Throne Room': '',
    'Wash Room': '',
    'Armory': '',
    'Temple': '',
    'Necropolis': '',
    'Wine Cellar': '',
    'Courtyard': '',
    'Sleeping Quarters': '',
    'Aslyum': '',
    'Sevants Quarters': '',
}

#TODO artifact room and treasure rooms have special good loot

while room_count < num_rooms:
    name, desc = random.choice(list(names_descriptions.items()))
    if room_count is 0:
        room = Room(title = name, description = desc)
        rooms.append(room)
        room_count += 1
    rand_room = rooms[random.randint(0, len(rooms) - 1)]
    dir = random.randint(0, 3)
    rand_dir = dirs[dir]
    rev_dir = reverse_dirs[dir]
    if rand_dir is 'n':
        if rand_room.n_to is 0:
            new_room = Room(title = name,
                            description = desc)
            new_room.save()
            rand_room.connectRooms(new_room, rand_dir)
            new_room.connectRooms(rand_room, rev_dir)
            new_room.save()
            rooms.append(new_room)
            room_count += 1
    elif rand_dir is 's': #dibs on refactoring these elifs<<<
        if rand_room.s_to is 0:
            new_room = Room(title = name,
                            description = desc)
            new_room.save()
            rand_room.connectRooms(new_room, rand_dir)
            new_room.connectRooms(rand_room, rev_dir)
            new_room.save()
            rooms.append(new_room)
            room_count += 1
    elif rand_dir is 'e':
        if rand_room.e_to is 0:
            new_room = Room(title = name,
                            description = desc)
            new_room.save()
            rand_room.connectRooms(new_room, rand_dir)
            new_room.connectRooms(rand_room, rev_dir)
            new_room.save()
            rooms.append(new_room)
            room_count += 1
    elif rand_dir is 'w':
        if rand_room.w_to is 0:
            new_room = Room(title = name,
                            description = desc)
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
