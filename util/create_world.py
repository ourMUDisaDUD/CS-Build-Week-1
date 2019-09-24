from django.contrib.auth.models import User
from adventure.models import Player, Room
import random

Room.objects.all().delete()

r_outside = Room(title="Outside Cave Entrance",
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
r_treasure.save()


existing_rooms = [r_foyer, r_overlook, r_overlook, r_narrow, r_treasure,]
added_rooms = []
num_rooms = 20
rooms = 0
dirs = {0: 'n', 1: 's', 2: 'e', 3:'w'}

while rooms < num_rooms:
  room = existing_rooms[random.randint(0, len(existing_rooms) - 1)]
  rand_dir = dirs[random.randint(0, 3)]
  if rand_dir is 'n':
    if room.n_to is 0:
      new_room = existing_rooms[random.randint(0, len(existing_rooms) - 1)]
      room.connect_rooms(new_room, rand_dir)
      added_rooms.append(new_room)
      rooms += 1
  if rand_dir is 's':
    if room.s_to is 0:
      new_room = existing_rooms[random.randint(0, len(existing_rooms) - 1)]
      room.connect_rooms(new_room, rand_dir)
      added_rooms.append(new_room)
      rooms += 1
  if rand_dir is 'e':
    if room.e_to is 0:
      new_room = existing_rooms[random.randint(0, len(existing_rooms) - 1)]
      room.connect_rooms(new_room, rand_dir)
      added_rooms.append(new_room)
      rooms += 1
  if rand_dir is 'w':
    if room.w_to is 0:
      new_room = existing_rooms[random.randint(0, len(existing_rooms) - 1)]
      room.connect_rooms(new_room, rand_dir)
      added_rooms.append(new_room)
      rooms += 1

players=Player.objects.all()
for p in players:
  p.currentRoom=r_foyer.id
  p.save()

