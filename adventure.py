import random
import time
import textwrap
import pygame

def winning():
	pygame.init()

	black = (0, 0, 0)
	white = (255, 255, 255)

	size=[700, 700]
	screen=pygame.display.set_mode(size)

	pygame.display.set_caption("You escaped!")

	snow_list=[]

	for i in range(50):
		x=random.randrange(0, 700)
		y=random.randrange(0, 700)
		snow_list.append([x, y])

	#Loop until user clicks the close button
	done=False

	clock=pygame.time.Clock()

	# Main Program Loop
	while done==False:
		### ALL EVENT PROCESSING ###
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done=True
		
		# All drawing code #
		screen.fill(black)

		for i in range(len(snow_list)):
			pygame.draw.circle(screen, white, snow_list[i], 2)
			snow_list[i][1] += 1
			if snow_list[i][1] > 700:
				y=random.randrange(-50, 10)
				snow_list[i][1]=y
				x=random.randrange(0, 700)
				snow_list[i][0]=x

		font=pygame.font.SysFont('Calibri', 35, True, False)

		text = font.render("You've Escaped!", True, white)
		text_rect = text.get_rect()
		text_x = screen.get_width() / 2 - text_rect.width / 2
		text_y = screen.get_height() / 2 - text_rect.height / 2
		screen.blit(text, [text_x, text_y])

		# MUST HAPPEN AFTER all drawing commands - updates screen
		pygame.display.flip()

		# Limit to 20 frames per second
		clock.tick(20)

	pygame.quit()


SOUTH = "south"
NORTH = "north"
WEST = "west"
EAST = "east"
DESC = "desc"

def startRoomDesc():
	print("You wake up in a dark room.")
	time.sleep(2)
	print("Sigh... Again.")
	time.sleep(2)
	print("You wait for your eyes to settle and see two doors. One to your west, and one to your east.")
	time.sleep(2)
	print("You can hear faint screams echoing out of the door in the west. The door on the right has a terrible smell coming out in waves.")
	time.sleep(2)
	print("West or East, which one will you take?")

worldRooms = {
	"Start Room": {
        # DESC: startRoomDesc(),
		DESC: "You wake up in a dark room. Sigh... Again. You wait for your eyes to settle and see two doors. One to your west, and one to your east. You can hear faint screams echoing out of the door in the west. The door in the east has a terrible smell coming out in waves. West or East, which one will you take?",
        WEST: "Sewer Pipe",
        EAST: "Monster Room Start"
	},
	"Monster Room Start": {
		DESC: "You open the east door... You fight the urge to vomit from the intensity of the stench that now envelopes you. Oh my god...did you just hear the door lock behind you? Fighting panic, you inch down the hallway... You see a massive pulsating mass at the end of the hallway...and the faint outline of another door just behind it. As you get closer, the monster wakes up. It stares at you, blinks, and dares you to take one step closer, to make his day.",
		WEST: "Monster Dead End",
		EAST: "Death"
	},
    "Sewer Pipe": {
        DESC: "You open the west door... To the west, the sewer slopes downward at a steep angle. It's full of water and you would have to swim. To the east, the sewer slopes gently upward, and is dry. To the north, the sewer continues for about twenty feet and seems to end.",
        WEST: "Swimming",
        EAST: "Monster Room From Sewer",
		NORTH: "Ladder"
	},
	"Monster Room Sewer": {
		DESC: "The smart thing to do in a sewer is to stay OUT of the water. And to try not to think about what's in that water. Ewwwww. You head east, trying to find your way out. A monster blocks your way. It dares you to take one step closer, to make his day.",
		WEST: "Monster Dead End",
		EAST: "Monster Dead End",
		NORTH: "Death"
	},
	"Swimming": {
		DESC: "Though not as skilled as Guybrush Threepwood™, you are quite capable of holding your breath underwater, even when that water is fetid and smelly. You swim down, down, down, until your lungs want to burst! Finally, you get past the obstructions and are able to swim back to the surface. You tread water and look around you. You could swim north. The water's flowing that way, so there might be a way out. You could swim west -- against the tide. east would take you back the way you came, which would probably hurt your lungs.",
		WEST: "Return Swimming West",
		EAST: "Return Swimming East",
		NORTH: "Escape"
	},
	"Ladder": {
		DESC: "Just as you thought: twenty feet further on, the tunnel ends. However, there's a ladder leading upwards - all you have to do is push the manhole cover up, and freedom is yours!",
		NORTH: "Manhole",
		SOUTH: "Sewer Pipe"
	},
	"Manhole": {
		DESC: "You climb the ladder and push the manhole cover up. Oh dear... a car must have parked on top of it. You can't get out. All is not lost, though; you discover a pair of gloves hanging over one of the rungs of the ladder. You take them and put them on. You feel a strange tingly sensation all over...and suddenly bold, SO BOLD. You glare at the manhole cover and ready yourself to shove it aside, parked car and all.",
		NORTH: "Escape Manhole"
	},
	"Monster Dead End": {
		DESC: "There\'s nowhere else to go - just past the monster, or back the way you came.",
		WEST: "Monster Dead End",
		EAST: "Monster Dead End",
		NORTH: "Death"
	},
	"Return Swimming West": {
		DESC: "The sewer narrows, forcing the water to move faster. You lose headway and allow yourself to drift back to where you were.",
		WEST: "Return Swimming West",
		EAST: "Return Swimming East",
		NORTH: "Escape"
	},
	"Return Swimming East": {
		DESC: "You dive under the water, but your lungs drag you back up to the surface. They're not going to let you do THAT swim again.",
		WEST: "Return Swimming West",
		EAST: "Return Swimming East",
		NORTH: "Escape"
	},
	"Death": {
		DESC: "You defiantely step forward. The monster's day is indeed made. He crushes your skull like a sparrow's egg between his thighs. You die. Fortunately, you saved your game before trying something this dangerous, so you quickly reload."
	},
	"Escape": {
		DESC: "You swim northwards and find yourself deep underwater, but with the sounds of splashing near you! If only you could get past this pile of rocks that's blocking your way... but it's too dark to see anything. Suddenly a man appears out of the shadows. With what are probably his last words, he informs you that his name is not Flynn, but Eugene. He sighs with regret at the actions that led him to this point. A blonde girl materializes beside him and inexplicably starts singing... Something about a glowing flower. Weird isn't it, what some people do with their last breaths? The girl's hair starts glowing! Hooray! You can now see where the water is flowing, and can remove the stones and escape! The three of you wash up on the bank of a river. Congratulations! Not only have you escaped the maze, you even found the lost princess! Of course, she doesn't know it yet, but that's another story altogether... "
	},
	"Escape Manhole": {
		DESC: "You blast shove aside manhole, car, and a surprised bird roosting on top of the vehicle with ease. You leap out of the hole and scream in victory!!"
	}
}

room = "Start Room"
screen_width = 80

def displayRoom(room):
	print(" ")
	print(room)
	print("=" * len(room))
	print(" ")
	# print(worldRooms[room][DESC])
	print("\n".join(textwrap.wrap(worldRooms[room][DESC], screen_width)))

	exits = []
	for direction in (WEST, EAST, NORTH, SOUTH):
		if direction in worldRooms[room].keys():
			exits.append(direction.title())
	print(" ")
	print("Exits: %s" % " ".join(exits))
	

def movePath(direction):
	global room
	if direction in worldRooms[room]:
		print("You move to the %s." % direction)
		room = worldRooms[room][direction]

def choosePath():
	path = ""
	while path != "west" and path != "east" and path != "north" and path != "south" and path != "quit":  #input validation to make sure people don't enter nonsense
		path = input("Which path will you choose? :  ")

	return path


playAgain = "yes"
while playAgain == "yes" or playAgain =="y":
	displayRoom(room)
	choice = choosePath()
	if choice == "quit":
		break
	if choice in (WEST, EAST, SOUTH, NORTH):
		movePath(choice)
	else:
		print("That is not a valid path.")
	
	if room == "Escape" or room == "Escape Manhole":
		winning()
		playAgain = input("Do you want to play again? yes or y to continue playing: ")
		room = "Start Room"
	if room == "Death":
		displayRoom(room)
		playAgain = input("Do you want to play again? yes or y to continue playing: ")
		room = "Start Room"



##CHRIS QUESTIONS
#How to do time.sleep() for the string blocks? I tried to call the fu
#How to change flow or room sequence for dead ends? Or if you get swept back to where you started like in the sewer?