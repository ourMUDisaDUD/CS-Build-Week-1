from django.contrib.auth.models import User
from adventure.models import Player, Room
import random

Room.objects.all().delete()

"""r_outside = Room(title="Outside Cave Entrance",
               description="North of you, the cave mount beckons")

r_foyer = Room(title="Foyer", description="""Dim light filters in from the south. Dusty
passages run north and east.""")

r_overlook = Room(title="Grand Overlook", description="""A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""")

r_narrow = Room(title="Narrow Passage", description="""The narrow passage bends here from west
to north. The smell of gold permeates the air.""")

r_treasure = Room(title="Treasure Chamber", description="""You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")

r_outside.save()
r_foyer.save()
r_overlook.save()
r_narrow.save()
r_treasure.save()"""


room_count = 0
rooms = []
dirs = {0: 'n', 1: 's', 2: 'e', 3:'w'}
num_rooms = 20
while room_count < num_rooms:
  if room_count is 0:
    room = Room(room_count, "A Generic Room", "This is a generic room.")
    rooms.append(room)
    room_count += 1
  rand_room = rooms[random.randint(0, len(rooms) - 1)]
  rand_dir = dirs[random.randint(0, 3)]
  if rand_dir is 'n':
    if rand_room.n_to is None:
      new_room = Room(room_count, "A Generic Room", "This is a generic room.")
      rand_room.connect_rooms(new_room, rand_dir)
      rooms.append(new_room)
      room_count += 1
  elif rand_dir is 's':
    if rand_room.s_to is None:
      new_room = Room(room_count, "A Generic Room", "This is a generic room.")
      rand_room.connect_rooms(new_room, rand_dir)
      rooms.append(new_room)
      room_count += 1
  elif rand_dir is 'e':
    if rand_room.e_to is None:
      new_room = Room(room_count, "A Generic Room", "This is a generic room.")
      rand_room.connect_rooms(new_room, rand_dir)
      rooms.append(new_room)
      room_count += 1
  elif rand_dir is 'w':
    if rand_room.w_to is None:
      new_room = Room(room_count, "A Generic Room", "This is a generic room.")
      rand_room.connect_rooms(new_room, rand_dir)
      rooms.append(new_room)
      room_count += 1
for room in rooms:
  room.save()

players=Player.objects.all()
for p in players:
  p.currentRoom=rooms[0].id
  p.save()