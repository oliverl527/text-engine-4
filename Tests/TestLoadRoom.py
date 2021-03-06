from Util.RoomUtil import *

import os
import unittest

PROJECT_DIR = os.path.abspath(os.path.join(os.path.join(__file__, os.pardir), os.pardir))
os.chdir(PROJECT_DIR)


class TestLoadRoom(unittest.TestCase):
    def test_load_room(self):
        test_room = load_room("Test Room")

        expected_room_name = "Test Room"
        self.assertEqual(expected_room_name, test_room.room_name)

        expected_room_file = "./Rooms/Test_Room.room"
        self.assertEqual(expected_room_file, test_room.room_file)

        expected_room_description = "This is the room's description"
        self.assertEqual(expected_room_description, test_room.description)

        expected_room_illumination = True
        self.assertEqual(expected_room_illumination, test_room.illuminated)

        expected_exit_size = 4
        self.assertEqual(expected_exit_size, len(test_room.exits))

        expected_inventory = []
        self.assertEqual(expected_inventory, test_room.inventory)

        expected_triggers = []
        self.assertEqual(expected_triggers, test_room.triggers)

    # TODO Don't require user input.
    def test_invalid_room_load(self):
        test_room = load_room("Room that doesn't exist")
        self.assertEqual(None, test_room)

        test_room = load_room()
        self.assertEqual(None, test_room)


if __name__ == "__main__":
    unittest.main()
