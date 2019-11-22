from django.contrib.auth.models import User
from adventure.models import Player, Room
from .rooms import make_rooms, make_descriptions

Room.objects.all().delete()

class World:
    def __init__(self):
        self.grid = None
        self.width = 0
        self.height = 0
    def generate_rooms(self, size_x, size_y, num_rooms):
        '''
        Fill up the grid, bottom to top, in a zig-zag pattern
        '''
        # Initialize the grid
        self.grid = [None] * size_y
        self.width = size_x
        self.height = size_y
        for i in range( len(self.grid) ):
            self.grid[i] = [None] * size_x

        # Start from lower-left corner (0,0)
        x = -1 # (this will become 0 on the first step)
        y = 0
        room_count = 0

        # Start generating rooms to the east
        direction = 1  # 1: east, -1: west

        # While there are rooms to be created...
        previous_room = None
        while room_count < num_rooms:

            # Calculate the direction of the room to be created
            if direction > 0 and x < size_x - 1:
                room_direction = "e"
                x += 1
            elif direction < 0 and x > 0:
                room_direction = "w"
                x -= 1
            else:
                # If we hit a wall, turn north and reverse direction
                room_direction = "n"
                y += 1
                direction *= -1

            # Create a room in the given direction
            # room = Room(room_count + 1, title = "A Generic Room", description = "This is a generic room.", x = x, y = y)
            # Note that in Django, you'll need to save the room after you create it
            room = Room(room_count + 1, title = make_rooms(), description = make_descriptions(), x = x , y = y)
            # Save the room in the World grid
            self.grid[y][x] = room

            # Connect the new room to the previous room
            if previous_room is not None:
                previous_room.connect_rooms(room, room_direction)
                # previous_room.connect_rooms(room, room_direction)
                # previous_room.save()
            
            # Update iteration variables
            previous_room = room
            room_count += 1
        # print('room grid', self.grid)
            # room.save()
        
    def print_rooms(self):
        '''
        Print the rooms in room_grid in ascii characters.
        '''

        # Add top border
        str = "# " * ((3 + self.width * 5) // 2) + "\n"

        # The console prints top to bottom but our array is arranged
        # bottom to top.
        #
        # We reverse it so it draws in the right direction.
        reverse_grid = list(self.grid) # make a copy of the list
        reverse_grid.reverse()
        for row in reverse_grid:
            # PRINT NORTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.n_to is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"
            # PRINT ROOM ROW
            str += "#"
            for room in row:
                if room is not None and room.w_to is not None:
                    str += "-"
                else:
                    str += " "
                if room is not None:
                    str += f"{room.id}".zfill(3)
                else:
                    str += "   "
                if room is not None and room.e_to is not None:
                    str += "-"
                else:
                    str += " "
            str += "#\n"
            # PRINT SOUTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.s_to is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"

        # Add bottom border
        str += "# " * ((3 + self.width * 5) // 2) + "\n"

        # Print string
        print(str)


w = World()
num_rooms = 100
width = 10
height = 10
w.generate_rooms(width, height, num_rooms)
w.print_rooms()


print(f"\n\nWorld\n  height: {height}\n  width: {width},\n  num_rooms: {num_rooms}\n")

# Room.objects.all().delete()

# class World:
#     def __init__(self):
#         self.grid = None
#         self.width = 0
#         self.height = 0


#     def generate_rooms(self, size_x, size_y, num_rooms):
#         # Fill up the grid, bottom to top, in a zig-zag pattern

#         # Initialize the grid
#         self.grid = [None] * size_y
#         self.width = size_x
#         self.height = size_y
#         for i in range( len(self.grid) ):
#             self.grid[i] = [None] * size_x

#         # Start from lower-left corner (0,0)
#         x = -1 # (this will become 0 on the first step)
#         y = 0
#         room_count = 0

#         # Start generating rooms to the east
#         direction = 1  # 1: east, -1: west

#         # While there are rooms to be created...
#         previous_room = None
#         while room_count < num_rooms:

#             # Calculate the direction of the room to be created
#             if direction > 0 and x < size_x - 1:
#                 room_direction = "e"
#                 x += 1
#             elif direction < 0 and x > 0:
#                 room_direction = "w"
#                 x -= 1
#             else:
#                 # If we hit a wall, turn north and reverse direction
#                 room_direction = "n"
#                 y += 1
#                 direction *= -1

#             # Create a room in the given direction
#             room = Room(room_count, make_rooms(), make_description(), x, y)
#             # Note that in Django, you'll need to save the room after you create it
#             # Save the room in the World grid
#             self.grid[y][x] = room
#             room.save()
            
            

#             # Connect the new room to the previous room
#             if previous_room is not None:
#                 previous_room.connect_rooms(room, room_direction)

#             # Update iteration variables
#             previous_room = room
#             room_count += 1

            

#         print('room grid', self.grid)
    
#     def print_rooms(self):
#         '''
#         Print the rooms in room_grid in ascii characters.
#         '''

#         # Add top border
#         str = "# " * ((3 + self.width * 5) // 2) + "\n"

#         # The console prints top to bottom but our array is arranged
#         # bottom to top.
#         #
#         # We reverse it so it draws in the right direction.
#         reverse_grid = list(self.grid) # make a copy of the list
#         reverse_grid.reverse()
#         for row in reverse_grid:
#             # PRINT NORTH CONNECTION ROW
#             str += "#"
#             for room in row:
#                 if room is not None and room.n_to is not None:
#                     str += "  |  "
#                 else:
#                     str += "     "
#             str += "#\n"
#             # PRINT ROOM ROW
#             str += "#"
#             for room in row:
#                 if room is not None and room.w_to is not None:
#                     str += "-"
#                 else:
#                     str += " "
#                 if room is not None:
#                     str += f"{room.id}".zfill(3)
#                 else:
#                     str += "   "
#                 if room is not None and room.e_to is not None:
#                     str += "-"
#                 else:
#                     str += " "
#             str += "#\n"
#             # PRINT SOUTH CONNECTION ROW
#             str += "#"
#             for room in row:
#                 if room is not None and room.s_to is not None:
#                     str += "  |  "
#                 else:
#                     str += "     "
#             str += "#\n"

#         # Add bottom border
#         str += "# " * ((3 + self.width * 5) // 2) + "\n"

#         # Print string
#         print(str)


# # r_outside = Room(title="Outside Cave Entrance",
# #                description="North of you, the cave mount beckons")

# # r_foyer = Room(title="Foyer", description="""Dim light filters in from the south. Dusty
# # passages run north and east.""")

# # r_overlook = Room(title="Grand Overlook", description="""A steep cliff appears before you, falling
# # into the darkness. Ahead to the north, a light flickers in
# # the distance, but there is no way across the chasm.""")

# # r_narrow = Room(title="Narrow Passage", description="""The narrow passage bends here from west
# # to north. The smell of gold permeates the air.""")

# # r_treasure = Room(title="Treasure Chamber", description="""You've found the long-lost treasure
# # chamber! Sadly, it has already been completely emptied by
# # earlier adventurers. The only exit is to the south.""")

# # r_testy = Room(title="BOiiii", description="if you don't...")

# # # 

# # r_outside.save()
# # r_foyer.save()
# # r_overlook.save()
# # r_narrow.save()
# # r_treasure.save()
# # r_testy.save()

# # Link rooms together
# # r_outside.connectRooms(r_foyer, "n")
# # r_foyer.connectRooms(r_outside, "s")

# # r_foyer.connectRooms(r_overlook, "n")
# # r_overlook.connectRooms(r_foyer, "s")

# # r_foyer.connectRooms(r_narrow, "e")
# # r_narrow.connectRooms(r_foyer, "w")

# # r_narrow.connectRooms(r_treasure, "n")
# # r_treasure.connectRooms(r_narrow, "s")

# # r_treasure.connectRooms(r_testy, "e")
# # r_testy.connectRooms(r_treasure, 'w')



# players=Player.objects.all()
# for p in players:
#   p.currentRoom= 1
#   p.save()

# w = World()
# num_rooms = 10
# width = 4
# height = 6
# w.generate_rooms(width, height, num_rooms)
# w.print_rooms()

# print(f"\n\nWorld\n  height: {height}\n  width: {width},\n  num_rooms: {num_rooms}\n")






