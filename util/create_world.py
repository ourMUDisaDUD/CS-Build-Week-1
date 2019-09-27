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
    'Bossroom': 'A large man stands in he middle of the room, he looks quite angry...',
    'Foyer': 'A spacious room that leads into other rooms',
    'Cliff': 'This room opens up to a cliff overlooking a small inlet, you feel a breeze from the north...',
    'Dragons Nest': 'A small room filled with Dragon eggs, one of them appears cracked...',
    'Narrow Passage': 'As you shimmey through this small corridor, you see light ahead...',
    'Infirmary': 'Heal your injuries here...',
    'Pantry': 'This room is filled to the brim with food, your lucky day.',
    'Library': 'A large room with shelves of books lined up on your left and right.',
    'Artifact Room': 'The floor shimmers as you walk around the room, there could be some priceless artifacts in here...',
    'Potions Room': 'This small room has been heavily used, you wonder if the Alchemist that made this mess is still around...',
    'Summoning Room': 'You enter to a grizzly scene, the smell makes you want to leave as soon as possible...',
    'Workshop': 'Here you may craft new items or upgrades.',
    'Trading Post': 'As you enter this room, you are greated with the sounds and smells of a small trading post.',
    'Hound Room': 'You hear barking in the distance. The bones on the ground don\'t look like dog treats',
    'Forge': 'A wave of heat hits your face as you enter this room, you see a multitude of tools and materials lying about. You see a blacksmith resting in the corner...',
    'Throne Room': 'An ornate chair sits lonely in the middle of this grandiose chamber...',
    'Wash Room': 'As you pass through, a musty smell lingers in the air, a broken wash basin lies long forgotten in the corner...',
    'Armory': 'Weapon racks line the walls with shimmering armor being displayed throughout. They seem to be recentley polished...',
    'Shrine': 'As you enter this room, softly illuminated by candles, a large stone statue looms overhead. There are many offerings at its feet...',
    'Necropolis': 'As you enter this crypt, a chill goes through your bones, you feel like you\'re being watched...',
    'Wine Cellar': 'The walls of this room are lined with shelves in a honeycomb pattern, some bottles still sit upon the shelves, though many are broken...',
    'Courtyard': 'You round a corner to moonlight illuminating a small enclosed yard, the smell of fresh air is a warm welcome.',
    'Sleeping Quarters': 'This room seemed to be the home of many travelers, you find that resting here would be a good idea.',
    'Servants Quarters': 'This run down room looks like it was not kept even while it was in regular use. Resting here may not restore full health...',
    'Training Room': 'Hone your combat skills here.',
    'Noble Quarters': 'Still shiny and glimmering, this room once housed a Noble or two. Though it seems like it\'s yours for the time being you don\'t exactly feel welcome...',
    'Hole in the wall': 'This incomplete room has no exits, but there is a hole in the wall that leads somewhere...'
}

end_finish = {
    'Entrance': 'You see an opening to the dungeon, you take a deep breath and venture forwards...',
    'Exit': 'You come to a large staircase leading to the outside, you have escaped this dungeon, for now...'
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
key = 1
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
            new_y = rand_room.y - 1
            new_room = Room(key = key, title = name, description = desc, x = rand_room.x, y = new_y)
            if f'{new_room.x},{new_room.y}' in cords.keys():  
                pass
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
            new_y = rand_room.y + 1
            new_room = Room(key = key, title = name, description = desc, x = rand_room.x, y = new_y)
            if f'{new_room.x},{new_room.y}' in cords.keys():  
                pass
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
                pass
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
                pass
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