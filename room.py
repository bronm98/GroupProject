import random
class Monster:
	def __init__(self, name):
		self.name = name

class Room:
	# individual room
	# contains a type & variables for a monster, item and 
	# a boolean for whether or not there are stairs there
	monster = None
	item = None
	stairs = False

	def __init__(self, level_type):
		self.level_type = level_type

	def add_monster(self, monster):
		self.monster = monster

class Floor:
	# 3 x 3 group of rooms
	# randomly generated with monsters (placeholder atm) & items
	# one room is assigned as an exit
	rooms = []
	def __init__(self, level_type):
		for x in range(0,9):
			self.rooms.append(Room(level_type))
		for i in range(0,random.randrange(1,4)):
			i = random.randrange(0,9)
			if self.rooms[i].monster == None:
				self.rooms[i].add_monster(Monster("jeff"))
		self.rooms[random.randrange(0,9)].stairs = True

	def print_map(self):
		# prints the layout of the map
		print("MAP:")
		output = ""
		for x in range(0,9):
			if self.rooms[x].stairs:
				output += "|/"
			elif self.rooms[x].monster != None:
				output += "|X"
			else:
				output += "| "

			if (x+1) % 3 == 0:
				print(output + "|")
				output = ""

	def describe_room(self, room):
		# Prints a description of the room
		output = "You are in the "
		if room < 3:
			output += "North "
		elif room > 5:
			output += "South "

		if (room+1) %3 == 0:
			output += "East "
		elif (room+1) %3 == 1:
			output += "West "

		if output == "You are in the ":
			output += "centre of the level"
		else:
			output += "side of the level" 

		print(output)



floor = Floor("type")
floor.print_map()

