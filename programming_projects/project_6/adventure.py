"""
Cole Leavitt
CSC110 Project -6
This program is a text-based adventure game. It loads game data from text files,
allows the user to interact with the game world, and keeps track of the user's
progress and inventory.
"""


def load_game():
    """
    This function opens the game file, reads the data, and stores it in a
    dictionary.

    Args: None.

    Returns: game: A dictionary where the keys are integers and the values
    are lists of strings.
    """
    game_file = open("game.txt", "r")
    game = {}
    for line in game_file:
        key, *value = line.strip().split('\t')
        if int(key) in game:
            game[int(key)].extend(value)
        else:
            game[int(key)] = value
    game_file.close()
    return game


def load_objects():
    """
    This function opens the objects file, reads the data, and stores it in a
    dictionary.

    Args: None.

    Returns: objects: A dictionary where the keys are tuples of integers and
    the values are lists of strings.
    """
    object_file = open("objects.txt", "r")
    objects = {}
    for line in object_file:
        key1, key2, obj_name, *value = line.strip().split('\t')
        objects[(int(key1), int(key2), obj_name)] = value
    object_file.close()
    return objects


def load_travel_table():
    """
    This function opens the travel table file, reads the data, and stores it
    in a dictionary.

    Args: None.

    Returns: travel_table: A dictionary where the keys are tuples of integers
    and the values are strings.
    """
    travel_file = open("travel_table.txt", "r")
    travel_table = {}
    for line in travel_file:
        key1, key2, *value = line.strip().split('\t')
        travel_table[(int(key1), int(key2))] = ' '.join(value)
    travel_file.close()
    return travel_table


def print_instructions():
    """
    This function prints the instructions for the game from the
    instructions.txt file.

    Args: None.

    Returns: None.
    """
    f = open("instructions.txt", "r")
    print(f.read())
    f.close()


def get_location(location, game, objects, player_objects):
    """
    This function gets the next location from the game data.
    It doesn't return anything, it prints messages related to
    objects (if the user has them or not) and location information
    Args:
        location: integer
        game: dictionary with location and string information
        objects: dictionary of location, binary (0 or 1), and object name
        player_objects: list of strings
    Returns:
        None
    """
    # for each string associated with that location in the game
    # dictionary, print that line
    for line in game[location]:
        print(line)

    # check if location has an object associated with it
    for key, value in objects.items():
        # if there's an object associated with this location
        # and the possible action is to take it (0)
        # and user hasn't taken it yet, print message associate with
        # object
        if key[0] == location and key[1] == 0 and key[2] not in player_objects:
            print(value[0])

        # if there's an object associated with this location,
        # and we need to check if the user has it (1)
        if key[0] == location and key[1] == 1:
            if key[2] in player_objects:
                # user has the object
                print(value[1])
            else:
                # user does not have the object
                print(value[0])


def go_to_location(location, travel_table, objects, player_objects, answer):
    """
    This function checks for the user's input (their answer), the objects
    that are available for the users to take, and the objects the user
    has in their object list
    Args:
        location: integer
        travel_table: dictionary with current location, possible to go
                      location and verb that takes user to go location
        objects: dictionary of location, binary (0 or 1), and object name
        player_objects: list of strings
        answer: input from the user (string)
    Returns:
        next location (integer)
    """
    # check if user wants to take an object
    if "take" in answer.lower():
        for key in objects:
            # check if there's an object to take
            if key[0] == location and key[1] == 0:
                # add object to user's object list
                player_objects.append(key[2])

    # check if the user needs to have an object to proceed
    for key in objects:
        # if there's a needed object for this location
        # but the user does not have it, return current location 
        # meaning the user doesn't go anywhere
        if key[0] == location and key[1] == 1 and key[2] not in player_objects:
            return location

    # no objects to take or needed to go anywhere
    # check where to go based on user's answer
    for x_y, verb in travel_table.items():
        if x_y[0] == location and verb in answer.upper():
            return x_y[1]


def play_game():
    """
    This function is the main game playing function.
    It loads all text files for the game, and asks
    for the player's input
    """
    # load game.txt
    game = load_game()
    # load objects.txt
    objects = load_objects()
    # load travel_table.txt
    travel_table = load_travel_table()
    # player starts with no objects
    player_objects = []
    # player starts at location 0
    location = 0
    # get info for location 0
    get_location(location, game, objects, player_objects)
    # ask if player wants instructions
    answer = input("> ")
    if "y" in answer.lower():
        print_instructions()
    # go to location 1 (start game for real)
    location += 1
    # this is just a demo with 11 locations
    while location < 12:
        # print info on current location
        get_location(location, game, objects, player_objects)
        # request player input
        answer = input("> ")
        # extra line break
        print()
        # player can exit at any time by inputting "exit"
        if "exit" not in answer.lower():
            # player doesn't want to exit
            # get next location based on player's input
            where_to_go = go_to_location(location, travel_table, objects,
                                         player_objects, answer)
            # if a possible location was found
            if where_to_go:
                # change location
                location = where_to_go
        else:  # user entered "exit"
            location = 12
    print("This is the end of this game demo.")


def main():
    try:
        # Test load_game function
        game = load_game()
        assert isinstance(game, dict), "load_game() should return a dictionary"
        assert len(game) > 0, "load_game() should return a non-empty dictionary"

        # Test load_objects function
        objects = load_objects()
        assert isinstance(objects,
                          dict), "load_objects() should return a dictionary"
        assert len(
            objects) > 0, "load_objects() should return a non-empty dictionary"

        # Test load_travel_table function
        travel_table = load_travel_table()
        assert isinstance(travel_table,
                          dict), ("load_travel_table() should return a "
                                  "dictionary")
        assert len(
            travel_table) > 0, ("load_travel_table() should return a non-empty "
                                "dictionary")

        # Test print_instructions function
        # Since this function prints instructions and does not return anything,
        # we can only test if it runs without errors
        print_instructions()

        print("All tests passed successfully.")

    except AssertionError as e:
        print(f"Test failed: {e}")


if __name__ == "__main__":
    main()
