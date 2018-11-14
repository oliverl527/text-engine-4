from Util.RoomUtil import load_room
from Objects.Room import Room


class CommandExecutor:
    room = None
    player = None
    trigger_list = []

    def __init__(self, room, player):
        self.room = room
        self.player = player
        #for x in room.triggers:
        #    self.trigger_list.append(("room", x.trigger_command, x.description))


    def executor(self, parsed_string):
        #print("\n", self.room.room_name)
        if parsed_string[0] == "error":
            print(parsed_string[0],":", parsed_string[1])
        elif parsed_string[0] == "look":
            self.look_function()
        elif parsed_string[ 0] == "go":
            self.move_function(parsed_string)
        elif parsed_string[0] == "examine":
            self.examine_function(parsed_string)
        elif parsed_string[0] in ["open", "close"]:
            self.open_close_function(parsed_string)
        elif parsed_string[0] in ["lock", "unlock"]:
            self.lock_unlock_function(parsed_string)
#        elif parsed_string[0] == "take":
#            self.get_function() TODO add this with items

    def look_function(self):
        self.room.look()

        # TODO Come back to this when objects have been created.
        #for x in self.room.inventory:
         #   print(x)

    def move_function(self, parsed_string):
        compass_direction = parsed_string[1]
        room_exits = self.room.exits

        applicable_exit = None
        exit_exists = False

        for e in room_exits:
            if e.compass_direction == compass_direction:
                exit_exists = True
                if not e.blocked:
                    if e.door:
                        if e.door.is_open:
                            applicable_exit = e
                            break
                        elif e.door.lock and e.door.lock.is_locked:
                            print("The door seems to be locked.")
                        elif e.door.lock and not e.door.lock.is_locked:
                            print("The door is closed, but it doesn't seem to be locked.")
                        else:
                            print("The door blocks your path.")
                    else:
                        applicable_exit = e
                        break
                else:
                    print("There is something in the way.")

        if not exit_exists:
            print("There is no exit in that direction.")

        if applicable_exit:
            self.room.load(applicable_exit.links_to)
            print("You move to {}.".format(self.room.room_name))

    def examine_function(self, parsed_string):

        examined_item = parsed_string[1]

        if examined_item not in Room.inventory: #and examined_item not in Player.inventory: # TODO bring this back once items/player inventory exist.
            print("That doesn't seem to be here. What are you trying to examine?")

        # TODO bring things below this line in once items are implemented.
        #else:
            #for x in Item.master_inventory:
                #if x == examined_item:
                   # print (Item.item_description)

    def open_close_function(self, parsed_string):
        worked = False
        for x in self.room.exits:
            if x.compass_direction == parsed_string[1]:
                if parsed_string[0] == "open":
                    x.open_door()
                elif parsed_string[0] == "close":
                    x.close_door()
                worked = True
                break
        if not worked:
            print("That is not a valid exit, thus there was no door.")

    def lock_unlock_function(self, parsed_string):
        worked = False
        for x in self.room.exits:
            if x.compass_direction == parsed_string[1]:
                if parsed_string[0] == "lock":
                    x.lock_door()
                elif parsed_string[0] == "unlock":
                    x.unlock_door()
                worked = True
                break
        if not worked:
            print("That is not a valid exit, thus there was no door.")



#   def get_function(self, parsed_string, room):
# should remove item from room inventory and append to player inventory. Should check for all 4 command parts
# i.e. get thing from container