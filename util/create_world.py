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
    'Artifact Room': 'The floor shimmers as you walk around the room, there could be some priceless artifacts in here...',
    'Potions Room': '',
    'Summoning Room': '',
    'Workshop': '',
    'Trading Post': 'As you enter this room, you are greated with the sounds and smells of a small trading post.',
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

end_finish = {
    'Start': 'Start desc',
    'Finish': 'Finish room'
}

endfin = list(end_finish.items())

def save_room(room, new_room, rand_dir, reverse_dir):
    new_room.save()
    room.connectRooms(new_room, rand_dir)
    new_room.connectRooms(room, reverse_dir)
    new_room.save()

cords = {}

#TODO artifact room and treasure rooms have special good loot
x = 0
y = 0
key = 0
while room_count < num_rooms:
    name, desc = random.choice(list(names_descriptions.items()))
    if room_count is 0:
        start_name, start_desc = endfin[0]
        room = Room(key = key, title = start_name, description = start_desc, x=x, y=y)
        cords[f'{x},{y}'] = room
        room.save()
        rooms.append(room)
        room_count += 1
        key += 1
    else:   
        #rand_room = rooms[random.randint(0, len(rooms) - 1)]
        rand_room = rooms[random.randint(len(rooms) // 2, len(rooms) - 1)]
        direction = random.randint(0, 3)
        rand_dir = dirs[direction]
        rev_dir = reverse_dirs[direction]
        if rand_dir is 'n' and rand_room.n_to is 0:
            if room_count == num_rooms - 1:
                end_name, end_desc = endfin[1]
                name = end_name
                desc = end_desc
            new_y = rand_room.y + 1
            new_room = Room(key = key, title = name, description = desc, x = rand_room.x, y = new_y)
            if f'{new_room.x},{new_room.y}' in cords.keys():  
                room = cords[f'{new_room.x},{new_room.y}']
                rand_room.connectRooms(room, rand_dir)
                room.connectRooms(rand_room, rev_dir)
                room.save()
            else:  
                save_room(rand_room, new_room, rand_dir, rev_dir)
                cords[f'{new_room.x},{new_room.y}'] = new_room
                rooms.append(new_room)
                room_count += 1
                key += 1
        elif rand_dir is 's' and rand_room.s_to is 0:
            if room_count == num_rooms - 1:
                end_name, end_desc = endfin[1]
                name = end_name
                desc = end_desc
            new_y = rand_room.y - 1
            new_room = Room(key = key, title = name, description = desc, x = rand_room.x, y = new_y)
            if f'{new_room.x},{new_room.y}' in cords.keys():  
                room = cords[f'{new_room.x},{new_room.y}']
                # #save_room(rand_room, cords[f'{new_room.x},{new_room.y}'], rand_dir, rev_dir)
                rand_room.connectRooms(room, rand_dir)
                room.connectRooms(rand_room, rev_dir)
                room.save()
            else:  
                save_room(rand_room, new_room, rand_dir, rev_dir)
                cords[f'{new_room.x},{new_room.y}'] = new_room
                rooms.append(new_room)
                room_count += 1
                key += 1
        elif rand_dir is 'e' and rand_room.e_to is 0:
            if room_count == num_rooms - 1:
                end_name, end_desc = endfin[1]
                name = end_name
                desc = end_desc
            new_x = rand_room.x + 1
            new_room = Room(key = key, title = name, description = desc, x = new_x, y = rand_room.y)
            if f'{new_room.x},{new_room.y}' in cords.keys():  
                room = cords[f'{new_room.x},{new_room.y}']
                rand_room.connectRooms(room, rand_dir)
                room.connectRooms(rand_room, rev_dir)
                room.save()
            else:  
                save_room(rand_room, new_room, rand_dir, rev_dir)
                cords[f'{new_room.x},{new_room.y}'] = new_room
                rooms.append(new_room)
                room_count += 1
                key += 1
        elif rand_dir is 'w' and rand_room.w_to is 0:
            if room_count == num_rooms - 1:
                end_name, end_desc = endfin[1]
                name = end_name
                desc = end_desc
            new_x = rand_room.x - 1
            new_room = Room(key = key, title = name, description = desc, x = new_x, y = rand_room.y)
            if f'{new_room.x},{new_room.y}' in cords.keys():  
                room = cords[f'{new_room.x},{new_room.y}']
                rand_room.connectRooms(room, rand_dir)
                room.connectRooms(rand_room, rev_dir)
                room.save()
            else:  
                save_room(rand_room, new_room, rand_dir, rev_dir)
                cords[f'{new_room.x},{new_room.y}'] = new_room
                rooms.append(new_room)
                room_count += 1
                key += 1
        rand_room.save()

players = Player.objects.all()
for p in players:
    p.currentRoom = rooms[0].id
    p.save()