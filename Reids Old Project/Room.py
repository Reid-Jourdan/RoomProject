class Room:
    def __init__(self, name, description = "An Empty Room"):
        #every room has a name, exits, locations for the exits,
        #item, item desciptions, and grabbbales
        self.name = name
        self.description = description
        self.exits = []
        self.exitLocations = []
        self.items = []
        self.itemDescriptions = []
        self.grabbables = []
    
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

    #add to the lists
    def addExit(self, exit, room):
        self.exits.append(exit)
        self.exitLocations.append(room)

    def addItem(self, item, desciption):
        self.items.append(item)
        self.itemDescriptions.append(desciption)
    
    def delItem(self, item):
        index = self.items.index(item)
        self.items.pop(index)
        self.itemDescriptions.pop(index)

    def addGrabbable(self, item):
        self.grabbables.append(item)

    def delGrabbable(self, item):
        self.grabbables.remove(item)

    #room desciptions
    def __str__(self):
        s = f"This is the {self.name}.\n"
        s+= self.description
        s+= f"\nYou see: "
        for i in self.items:
            s += i + " "
        s += "\n"
        s += "Exits: "
        for e in self.exits:
            s += e + " "
        s += "\n"
        return s
    
##################################################
#HELPER FUNCTIONS


#make 4 rooms
whiteR = Room("White Room", "An empty room that has a rug at the door.")
blueR = Room("Blue Room", "A room painted a shade of blue with picture of the same man hanging all over.")
redR = Room("Red Room", "A crimson stained room with a bucket in the corner.")
greenR = Room("Green Room", "The room has green wall paper and there is a locked closet door.")
yellowR = Room("Yellow Room", "The walls are a sickening yellow and there is a shelf with lots of junk on it.")
closet = Room("Closet", "Through the darkness there is a statue of man name Ankunda Kiremire")

##add exits to rooms
whiteR.addExit("east", blueR)

blueR.addExit("east", redR)
blueR.addExit("west", whiteR)

redR.addExit("west", blueR)
redR.addExit("south", greenR)

greenR.addExit("north", redR)
greenR.addExit("south", yellowR)

yellowR.addExit("north", greenR)

closet.addExit("east", greenR)

#add grabbables and items to r1
whiteR.addItem("Rug", "It says \"GOODBYE\" insead of welcome and there is a slight bulge under it resembling a key")

blueR.addItem("Painting", "It looks something like https://ars.els-cdn.com/content/image/1-s2.0-S138912861400259X-fx1.jpg")
blueR.addItem("Trapdoor", "You slipped and fell into the void")

redR.addItem("Blood_Bucket", "It has murky red liquid inside and a faint shimmer of gold at the bottom")
redR.addGrabbable("blood")

greenR.addItem("Closet_Door", "It has three normal looking locks on it requiring 3 seperate keys")

yellowR.addItem("Large_Babushka", "You found a smaller one inside")

currentRoom = whiteR
    
def death():
    print(" " * 17 + "u" * 7)
    print(" " * 13 + "u" * 2 + "$" * 11 + "u" * 2)
    print(" " * 10 + "u" * 2 + "$" * 17 + "u" * 2)
    print(" " * 9 + "u" + "$" * 21 + "u")
    print(" " * 8 + "u" + "$" * 23 + "u")
    print(" " * 7 + "u" + "$" * 25 + "u")
    print(" " * 7 + "u" + "$" * 25 + "u")
    print(" " * 7 + "u" + "$" * 6 + "\"" + " " * 3 + "\"" + "$" * 3 + "\"" + " " * 3 + "\"" + "$" * 6 + "u")
    print(" " * 7 + "\"" + "$" * 4 + "\"" + " " * 6 + "u$u" + " " * 7 + "$" * 4 + "\"")
    print(" " * 8 + "$" * 3 + "u" + " " * 7 + "u$u" + " " * 7 + "u" + "$" * 3)
    print(" " * 8 + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3)
    print(" " * 9 + "\"" + "$" * 4 + "u" * 2 + "$" * 3 + " " * 3 + "$" * 3 + "u" * 2 + "$" * 4 + "\"")
    print(" " * 10 + "\"" + "$" * 7 + "\"" + " " * 3 + "\"" + "$" * 7 + "\"")
    print(" " * 12 + "u" + "$" * 7 + "u" + "$" * 7 + "u")
    print(" " * 13 + "u$\"$\"$\"$\"$\"$\"$u")
    print(" " * 2 + "u" * 3 + " " * 8 + "$" * 2 + "u$ $ $ $ $u" + "$" * 2 + " " * 7 + "u" * 3)
    print(" u" + "$" * 4 + " " * 8 + "$" * 5 + "u$u$u" + "$" * 3 + " " * 7 + "u" + "$" * 4)
    print(" " * 2 + "$" * 5 + "u" * 2 + " " * 6 + "\"" + "$" * 9 + "\"" + " " * 5 + "u" * 2 + "$" * 6)
    print("u" + "$" * 11 + "u" * 2 + " " * 4 + "\"" * 5 + " " * 4 + "u" * 4 + "$" * 10)
    print("$" * 4 + "\"" * 3 + "$" * 10 + "u" * 3 + " " * 3 + "u" * 2 + "$" * 9 + "\"" * 3 + "$" * 3 + "\"")
    print(" " + "\"" * 3 + " " * 6 + "\"" * 2 + "$" * 11 + "u" * 2 + " " + "\"" * 2 + "$" + "\"" * 3)
    print(" " * 11 + "u" * 4 + " \"\"" + "$" * 10 + "u" * 3)
    print(" " * 2 + "u" + "$" * 3 + "u" * 3 + "$" * 9 + "u" * 2 + " \"\"" + "$" * 11 + "u" * 3 + "$" * 3)
    print(" " * 2 + "$" * 10 + "\"" * 4 + " " * 11 + "\"\"" + "$" * 11 + "\"")
    print(" " * 3 + "\"" + "$" * 5 + "\"" + " " * 22 + "\"\"" + "$" * 4 + "\"\"")
    print(" " * 5 + "$" * 3 + "\"" + " " * 25 + "$" * 4 + "\"")
    print(" " * 14 + "You are dead")

def victory():
    print("You have won the game!")
    print("Click here to claim your reward: https://rb.gy/6hesmx")

def printRules():
    print("Welcome to the escape house! Thanks for playing.")
    print("Rules:\n\tYou have 3 lives")
    print("\tActions are \'go\', \'look\', and \'take\', use these to move around and interact with anything you see or maybe find...")
    print("\tIf you misspell a word, you lose a life.")
    print("\tFYI... beware of the basement.")
    


######################### MAIN #########################
inventory = []
doorUnlocked = False
hp = 3

printRules()

while(True):
    status = f"{currentRoom}\nYou are carrying: {inventory}\nYour current hp is: {hp}"

    if(currentRoom == None):
        death()
        break

    if(currentRoom == closet):
        victory()
        break

    print("="*40)
    print(status)

    action = input("What to do? ").lower().strip()

    if(action in ["quit", "bye", "exit", "leave"]):
        break

    response = "I don't understand. Try \"verb noun\". \nValid verbs are \"go\", \"look\", and \"take\""
    #parse what they typed
    words = action.split()

    if(len(words) == 2):
        verb = words[0]
        noun = words[1]

        #what happens if it is go
        if (verb == "go"):
            response = "invalid exit"
            #check all exits
            for i in range(len(currentRoom.exits)):
                if(noun == currentRoom.exits[i]):
                    #change location
                    currentRoom = currentRoom.exitLocations[i]
                    response = "\nRoom Changed"
                    break
        
        #if verb is look
        if (verb == "look"):
            response = "I don't see that item"

            #check items
            for i in range(len(currentRoom.items)):
                if noun.lower() == currentRoom.items[i].lower():
                    #give the correct response(desciption)
                    response = currentRoom.itemDescriptions[i]
                    if(noun == "closet_door"):
                        if(inventory.count("key") >= 3):
                            greenR.addExit("west", closet)
                            response = ("The door is now unlocked!")
                    if(noun == "large_babushka"):
                        yellowR.addItem("medium_babushka", "there is a smaller one inside")
                        yellowR.delItem("Large_Babushka")
                    if(noun == "medium_babushka"):
                        yellowR.addItem("small_babushka", "there was a key inside!")
                        yellowR.delItem("medium_babushka")
                    if(noun == "small_babushka"):
                        yellowR.addGrabbable("key")
                        yellowR.delItem("small_babushka")
                    if(noun == "rug"):
                        whiteR.addGrabbable("key")
                    if(noun == "blood_bucket"):
                        redR.addGrabbable("key")
                    if(noun == "trapdoor"):
                        currentRoom = None
                    break
        
        #if verb is take
        if (verb == "take"):
            response = "I don't see that item"
            #check room
            for grabbable in currentRoom.grabbables:

                if noun == grabbable:
                    #add to inventory
                    inventory.append(grabbable)
                    #remove from room
                    currentRoom.delGrabbable(grabbable)
                    response = "\nItem grabbed"
                    break
    if(response == "I don't see that item"):
        hp -= 1
    if(hp <= 0):
        currentRoom = None
    print(f"\n{response}")

