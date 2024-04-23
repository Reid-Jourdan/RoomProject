###########################################################################################
# Name: Jay Graham, Reid Jourdan, Nathan Silvernale, Dylan Ronquile
# Date: 4/29/2024
# Description: This program is a text-based adventure game. The player can move between rooms,
###########################################################################################
from tkinter import * 
from random import randint

# Define the Room class
class Room:
    def __init__(self, name, image):
        self.name = name
        self.image = image
        self.exits = {}
        self.items = {}
        self.grabbables = {}

    #name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    #room desciption
    @property
    def description(self):
        return self._description
    @description.setter
    def description(self, newDecription):
        self._description = newDecription
    
    #exits
    @property
    def exits(self):
        return self._exits
    @exits.setter
    def exits(self, exits):
        self._exits = exits
    
    #exit locations
    @property
    def exitLocations(self):
        return self._exitLocations
    @exitLocations.setter
    def exitLocations(self, newName):
        self._exitLocations = newName
    
    #items
    @property
    def items(self):
        return self._items
    @items.setter
    def items(self, items):
        self._items = items
    
    #item desciptions
    @property
    def itemDescriptions(self):
        return self._itemDescriptions
    @itemDescriptions.setter
    def itemDescriptions(self, itemDescriptions):
        self._itemDescriptions = itemDescriptions
    
    #grabbables
    @property
    def grabbables(self):
        return self._grabbables
    @grabbables.setter
    def grabbables(self, grabbables):
        self._grabbables = grabbables

    # Getters and setters for instance variables
    def addExit(self, exit, room):
        self.exits[exit] = room

    def addItem(self, item, desc):
        self.items[item] = desc

    def delItem(self, item):
        del self.items[item]

    def addGrabbable(self, item, desc):
        self.grabbables[item] = desc

    def delGrabbable(self, item):
        del self.grabbables[item]

    def __str__(self):
        s = "You are in {}.\n".format(self.name)
        s += "You see: "
        for item in self.items.keys():
            s += item + " "
        s += "\nExits: "
        for exit in self.exits.keys():
            s += exit + " "
        return s

class Person:
    def __init__(self, name, health, damage):
        self._name = name
        self._health = health
        self._damage = damage

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
    @property
    def health(self):
        return self._health
    @health.setter
    def health(self, health):
        self._health = health
    @property
    def damage(self):
        return self._damage
    @damage.setter
    def damage(self, damage):
        self._damage = damage

    def attack(self, other_person):
        if "bad-code_snippet" in Game.inventory:
            other_person.receive_damage(self._damage)
        else:
            print("You need a bad-code_snippet to attack!")

    def block(self):
        blocked_damage = random.randint(0, self._damage)
        print(f"{self._name} blocked {blocked_damage} damage.")
        return blocked_damage

    def receive_damage(self, damage):
        self._health -= damage
        if self._health < 0:
            self._health = 0
            print(f"{self._name} has been defeated.")

    def random_action(self, other_person):
        if random.choice(['attack', 'block']) == 'attack':
            self.attack(other_person)
        else:
            self.block()

class Boss(Person):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)

    def random_action(self, other_person):
        action = random.choice(['attack', 'block'])
        if action == 'attack':
            print(f"{self._name} attacks!")
            self.attack(other_person)
        else:
            print(f"{self._name} blocks!")
            self.block()

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
        # self.image.pack_propagate(False)

        text_frame = Frame(self, width=self.WIDTH // 2)
        self.text = Text(text_frame, bg="lightgrey", state=DISABLED)
        self.text.pack(fill=Y, expand=1)
        text_frame.pack(side=RIGHT, fill=Y)
        text_frame.pack_propagate(False)

    def createRooms(self):
        # Create room objects with names and associated images
        r0 = Room("Room 0", "start.png")
        r1 = Room("Room 1", "room1.gif")
        r2 = Room("Room 2", "room2.gif")
        r3 = Room("Room 3", "room3.gif")
        r4 = Room("Room 4", "room4.gif")
        r5 = Room("Room 5", "FinalBoss.png")
        r5 = Room("Room 5", "FinalBoss.png")

        # Add exits to each room
        r0.addExit("start", r1)

        r1.addExit("east", r2)
        r1.addExit("south", r3)

        r2.addExit("west", r1)
        r2.addExit("south", r4)

        r3.addExit("north", r1)
        r3.addExit("east", r4)

        r4.addExit("north", r2)
        r4.addExit("west", r3)
        r4.addExit("south", r5)  # Boss Exit

        # Add items and grabbables to each room
        r1.addGrabbable("key", "The key has a golden shine.")
        r1.addItem("chair", "It is made of wicker and no one is sitting on it.")
        r1.addItem("table", "It is made of oak. A golden key rests on it.\nThere is a piece of code-bullet1 on it.")
        r1.addGrabbable("code-bullet1", "The only weapon that can damage a professional\ncoder.")

        r2.addItem("rug", "It is nice and Indian. It also needs to be\nvacuumed. There is a gun shaped bulge under the\ncarpet.")
        r2.addItem("fireplace", "It is full of ashes.")
        r2.addGrabbable("gun", "A gun that shoots a particularly weird,\ncode-based bullet.")

        r3.addGrabbable("book", "It\'s about coding.")
        r3.addItem("bookshelves", "They are empty. Go figure. However, there is a\ncode-bullet3.")
        r3.addItem("statue", "There is nothing special about it. A shield is\nleaning against it.")
        r3.addItem("desk", "The statue is resting on it. So is a book as well as a code-bullet2.")
        r3.addGrabbable("shield", "A shield that looks like it will fall apart if\nanything strikes it.")
        r3.addGrabbable("code-bullet2", "The only weapon that can damage a professional\ncoder.")
        r3.addGrabbable("code-bullet3", "The only weapon that can damage a professional\ncoder.")

        r4.addGrabbable("6-pack", "It's coke, I swear.")
        r4.addItem("brew_rig", "Gourd is brewing some sort of oatmeal stout on\nthe brew rig. A 6-pack is resting beside it. As\nwell as a code-bullet4.")
        r4.addGrabbable("code-bullet4", "The only weapon that can damage a professional\ncoder.")


        r5.addItem("dr_bowman", "The immaculate Computer Science professor that\nwon't let you pass without a fight!")

        # Set initial room
        Game.currentRoom = r0

        # Initialize player's inventory
        Game.inventory = {}

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


    def setRoomImage(self, deathScreen = 'alive'):
        if Game.currentRoom is None:
            if deathScreen == 'dice':
                img = PhotoImage(file="dice.png")
            elif deathScreen == "goku": 
                img = PhotoImage(file="TakeTheL.gif")
            elif deathScreen == "victory":
                img = PhotoImage(file="victory.png")
            elif deathScreen == "easter":
                img = PhotoImage(file="easter.png")
            else:
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
        self.setRoomImage()
        self.setStatus("Welcome to a room Adventure! You have to explore to defeat a boss at the end of the dungeon! Type \"start\" to start the room adventure!\nProvided actions are:\n\'go\' - allows you to travel between rooms using\ncardinal directions\n\'look\' - allows you to look around the room, at\nitems in the room, and at items in your inventory\n\'take\' - allows you to grab that you see when\nlooking\n\'attack\' - allows you to attack an enemy.\nThere is a one in 20 chance of dying when moving from room to room, so beware!")
        self.hitsTaken = 0

    def start(self):
        Game.currentRoom = Game.currentRoom.exits["start"]
        self.setRoomImage()
        self.setStatus("")

    def process(self, event):
        playerHealth = 100
        bossHealth = 100

        if playerHealth == 0:
            self.currentRoom = None

        action = self.player_input.get()
        action = action.lower()
        words = action.split()

        status = ""

        if len(words) > 0:
            if words[0] == "start":
                self.start()
                status = str(Game.currentRoom)

            elif words[0] == "go":
                if len(words) > 1:
                    roll = randint(1, 20)
                    Game.currentRoom = Game.currentRoom.exits[words[1]]
                    status = str(Game.currentRoom)
                    if roll == 1:
                        Game.currentRoom = None
                        status = "You rolled a nat 1, so you tripped and died lol."
                    self.setRoomImage('dice')
                else:
                    status = "Go where?"
            elif words[0] == "look":
                if len(words) > 1:
                    if words[1] in Game.currentRoom.items:
                        status = Game.currentRoom.items[words[1]]
                    elif words[1] in Game.inventory:
                        status = Game.inventory[words[1]]
                    else:
                        status = "I don't see that item."
                else:
                    status = str(Game.currentRoom)

            elif words[0] == "take":
                if len(words) > 1:
                    if words[1] in Game.currentRoom.grabbables:
                        grab = words[1]
                        Game.inventory.update({grab : Game.currentRoom.grabbables[grab]})
                        Game.currentRoom.delGrabbable(words[1])
                        status = "Item taken."
                    else:
                        status = "I don't see that item."
                else:
                    status = "Take what?"
            elif words[0] == "attack":
                if len(words) > 1:
                    if int(self.currentRoom.name[-1]) == 5:
                        if words[1] == "dr_bowman":
                            if "gun" in Game.inventory:
                                if "code-bullet1" in Game.inventory:
                                    del Game.inventory["code-bullet1"]
                                    status = "You damaged Dr. Bowman"
                                    self.hitsTaken += 1
                                    if self.hitsTaken == 4:
                                        status = "YOU BEAT THE IMMACUALTE DR. BOWMAN"
                                        Game.currentRoom = None
                                        self.setRoomImage("victory")
                                elif "code-bullet2" in Game.inventory:
                                    del Game.inventory["code-bullet2"]
                                    status = "You damaged Dr. Bowman"
                                    self.hitsTaken += 1
                                    if self.hitsTaken == 4:
                                        status = "YOU BEAT THE IMMACUALTE DR. BOWMAN"
                                        Game.currentRoom = None
                                        self.setRoomImage("victory")
                                elif "code-bullet3" in Game.inventory:
                                    del Game.inventory["code-bullet3"]
                                    status = "You damaged Dr. Bowman"
                                    self.hitsTaken += 1
                                    if self.hitsTaken == 4:
                                        status = "YOU BEAT THE IMMACUALTE DR. BOWMAN"
                                        Game.currentRoom = None
                                        self.setRoomImage("victory")
                                elif "code-bullet4" in Game.inventory:
                                    del Game.inventory["code-bullet4"]
                                    status = "You damaged Dr. Bowman"
                                    self.hitsTaken += 1
                                    if self.hitsTaken == 4:
                                        status = "YOU BEAT THE IMMACUALTE DR. BOWMAN"
                                        Game.currentRoom = None
                                        self.setRoomImage("victory")
                                else:
                                    status = "You ran out of bullets and Dr. Bowman was able to use 1% of his power and you got evicerated off\nthe face of the planet"
                                    Game.currentRoom = None
                                    self.setRoomImage("goku")
                            else:
                                status = "You had nothing to attack with, so you ran in fist ablazing, and croaked. Maybe get a weapon next time!"
                                Game.currentRoom = None
                                self.setRoomImage("goku")
                    else:
                        status = "There is nothing in this room to attack"
                else:
                    status = "What do you want to attack?"
                
            elif words[0] == "die":
                Game.currentRoom = None
                self.setRoomImage()

            else:
                status = "Invalid command."
        
        status += f"\nInventory: {list(Game.inventory.keys())}"
        self.setStatus(status)
        self.player_input.delete(0, END)

# Main code
if __name__ == "__main__":
    window = Tk()
    window.title("Room Adventure")

    g = Game(window)
    g.play()

    window.mainloop()
    