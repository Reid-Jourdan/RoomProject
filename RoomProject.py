###########################################################################################
# Name: Dylan Ronquille	
# Date: 4/29/2024
# Description: This program is a text-based adventure game. The player can move between rooms,
###########################################################################################
from tkinter import * 

# Define the Room class
class Room:
    def __init__(self, name, image):
        self.name = name
        self.image = image
        self.exits = {}
        self.items = {}
        self.grabbables = []

    # Getters and setters for instance variables
    def addExit(self, exit, room):
        self.exits[exit] = room

    def addItem(self, item, desc):
        self.items[item] = desc

    def addGrabbable(self, item):
        self.grabbables.append(item)

    def delGrabbable(self, item):
        self.grabbables.remove(item)

    def __str__(self):
        s = "You are in {}.\n".format(self.name)
        s += "You see: "
        for item in self.items.keys():
            s += item + " "
        s += "\nExits: "
        for exit in self.exits.keys():
            s += exit + " "
        return s

# Define the Game class
class Game(Frame):
    WIDTH = 800
    HEIGHT = 600

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack(fill=BOTH, expand=1)

        self.player_input = Entry(self, bg="white")
        self.player_input.bind("<Return>", self.process)
        self.player_input.pack(side=BOTTOM, fill=X)
        self.player_input.focus()

        self.image = Label(self, width=self.WIDTH // 2)
        self.image.pack(side=LEFT, fill=Y)
        self.image.pack_propagate(False)

        text_frame = Frame(self, width=self.WIDTH // 2)
        self.text = Text(text_frame, bg="lightgrey", state=DISABLED)
        self.text.pack(fill=Y, expand=1)
        text_frame.pack(side=RIGHT, fill=Y)
        text_frame.pack_propagate(False)

    def createRooms(self):
        # Create room objects with names and associated images
        r1 = Room("Room 1", "room1.gif")
        r2 = Room("Room 2", "room2.gif")
        r3 = Room("Room 3", "room3.gif")
        r4 = Room("Room 4", "room4.gif")

        # Add exits to each room
        r1.addExit("east", r2)
        r1.addExit("south", r3)

        r2.addExit("west", r1)
        r2.addExit("south", r4)

        r3.addExit("north", r1)
        r3.addExit("east", r4)

        r4.addExit("north", r2)
        r4.addExit("west", r3)
        r4.addExit("south", None)  # Death exit

        # Add items and grabbables to each room
        r1.addGrabbable("key")
        r1.addItem("chair", "It is made of wicker and no one is sitting on it.")
        r1.addItem("table", "It is made of oak. A golden key rests on it.")

        r2.addItem("rug", "It is nice and Indian. It also needs to be vacuumed.")
        r2.addItem("fireplace", "It is full of ashes.")

        r3.addGrabbable("book")
        r3.addItem("bookshelves", "They are empty. Go figure.")
        r3.addItem("statue", "There is nothing special about it.")
        r3.addItem("desk", "The statue is resting on it. So is a book.")

        r4.addGrabbable("6-pack")
        r4.addItem("brew_rig", "Gourd is brewing some sort of oatmeal stout on the brew rig. A 6-pack is resting beside it.")

        # Set initial room
        Game.currentRoom = r1

        # Initialize player's inventory
        Game.inventory = []

    def setupGUI(self):
        self.pack(fill=BOTH, expand=1)

        self.player_input = Entry(self, bg="white")
        self.player_input.bind("<Return>", self.process)
        self.player_input.pack(side=BOTTOM, fill=X)
        self.player_input.focus()

        self.image = Label(self, width=self.WIDTH // 2)
        self.image.pack(side=LEFT, fill=Y)
        self.image.pack_propagate(False)

        text_frame = Frame(self, width=self.WIDTH // 2)
        self.text = Text(text_frame, bg="lightgrey", state=DISABLED)
        self.text.pack(fill=Y, expand=1)
        text_frame.pack(side=RIGHT, fill=Y)
        text_frame.pack_propagate(False)


    def setRoomImage(self):
        if Game.currentRoom is None:
            img = PhotoImage(file="skull.gif")
        else:
            img = PhotoImage(file=Game.currentRoom.image)
        self.image.config(image=img)
        self.image.image = img

    def setStatus(self, status):
        self.text.config(state=NORMAL)
        self.text.delete("1.0", END)
        self.text.insert(END, status)
        self.text.config(state=DISABLED)

    def play(self):
        self.createRooms()
        self.setupGUI()
        self.setRoomImage()
        self.setStatus("")

    def process(self, event):
        action = self.player_input.get()
        action = action.lower()
        words = action.split()

        if len(words) > 0:
            if words[0] == "go":
                if len(words) > 1:
                    Game.currentRoom = Game.currentRoom.exits[words[1]]
                    self.setRoomImage()
                    self.setStatus("")

                else:
                    self.setStatus("Go where?").__annotations__
            elif words[0] == "look":
                if len(words) > 1:
                    if words[1] in Game.currentRoom.items:
                        self.setStatus(Game.currentRoom.items[words[1]])
                    else:
                        self.setStatus("I don't see that item.")
                else:
                    self.setStatus(Game.currentRoom)

            elif words[0] == "take":
                if len(words) > 1:
                    if words[1] in Game.currentRoom.grabbables:
                        Game.inventory.append(words[1])
                        Game.currentRoom.delGrabbable(words[1])
                        self.setStatus("Item taken.")
                    else:
                        self.setStatus("I don't see that item.")
                else:
                    self.setStatus("Take what?")

            else:
                self.setStatus("Invalid command.")

        self.player_input.delete(0, END)

# Main code
if __name__ == "__main__":
    window = Tk()
    window.title("Room Adventure")

    g = Game(window)
    g.play()

    window.mainloop()
    