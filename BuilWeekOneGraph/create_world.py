# from django.contrib.auth.models import User
from adventure.models import Player, Room
from util.betterworld import World
import random
from ast import literal_eval

room_count = 0
Room.objects.all().delete()
r_outside = Room(room_count, title="Outside Cave Entrance", description="North of you, the cave mount beckons" ,x=0 , y=0)
r_foyer = Room(room_count, title="Foyer", description="""Dim light filters in from the south. Dusty passages run north and east.""", x =0, y = 1)
r_overlook = Room(room_count, title="Grand Overlook", description="""A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""", x=0, y=2)
r_narrow = Room(room_count, title="Narrow Passage", description="""The narrow passage bends here from west to north. The smell of gold permeates the air.""", x= -1 ,y= 0)
r_treasure = Room(room_count, title="Treasure Chamber", description="""You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""", x= -1, y = 2)

list1 = [] 
list1.append(r_outside)
list1.append(r_foyer)
list1.append(r_overlook)
list1.append(r_narrow)
list1.append(r_treasure)

list2 = [] 
list2.append(r_outside)
list2.append(r_foyer)
list2.append(r_overlook)
list2.append(r_narrow)
list2.append(r_treasure)





# take the last element of first list 
last_element_of_first_list = list1[-1]
first_element_of_second_list = list2[0]

print(last_element_of_first_list.title)
last= last_element_of_first_list.title
print(first_element_of_second_list.title)

first = first_element_of_second_list.title
#connect it to first element of next list




r_outside.save()
r_foyer.save()
r_overlook.save()
r_narrow.save()
r_treasure.save()
last_element_of_first_list.save()
first_element_of_second_list.save()
# Link rooms together
r_outside.connectRooms(r_foyer, "n")
r_foyer.connectRooms(r_outside, "s")
r_foyer.connectRooms(r_overlook, "n")
r_overlook.connectRooms(r_foyer, "s")
r_foyer.connectRooms(r_narrow, "e")
r_narrow.connectRooms(r_foyer, "w")
r_narrow.connectRooms(r_treasure, "n")
r_treasure.connectRooms(r_narrow, "s")
last_element_of_first_list.connectRooms(first_element_of_second_list, "w")



players = Player.objects.all()
for p in players:
    p.currentRoom = r_outside.id
    p.save()

for i in list1:
    print(f"{i.title} ( {i.x} , {i.y} )")
    
    
# world = World()
# map_file = "util/main_maze.txt"

# # Loads the map into a dictionary
# room_graph=literal_eval(open(map_file, "r").read())
# world.load_graph(room_graph)

import matplotlib.pyplot as plt
# Draw multiple points.
def draw_multiple_points():

    # x axis value list.
    x_number_list = []
    for x in list1:
        axis = int(x.x)
        x_number_list.append(axis)

    # y axis value list.
    y_number_list = []
    for y in list1:
        ycis = y.y
        y_number_list.append(ycis)
    # Draw point based on above x, y axis values.
    plt.scatter(x_number_list, y_number_list, s=10)

    # Set chart title.
    plt.title("Extract Number Root ")

    # Set x, y label text.
    plt.xlabel("Number")
    plt.ylabel("Extract Root of Number")
    plt.show()

if __name__ == '__main__':
    draw_multiple_points()