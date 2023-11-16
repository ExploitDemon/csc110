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
    # Open the file named "game.txt" in read mode
    with open("game.txt", "r", encoding="UTF-8") as game_file:

        # Initialize an empty dictionary to store the game data
        game = {}

        # Iterate over each line in the file
        for line in game_file:
            # Split the line into components based on the tab character The
            # first component is converted to an integer and used as a key in
            # the dictionary The rest of the components (if any) are stored
            # as a list of values
            key, *values = line.strip().split('\t')

            # If the key is already in the dictionary, append each value to the
            # list associated with the key
            if int(key) in game:
                for value in values:
                    game[int(key)].append(value)
            else:
                # If the key is not in the dictionary, add a new entry with the
                # key and the list of values
                game[int(key)] = values

    # Return the dictionary containing the loaded data
    return game


def load_objects():
    """
    This function opens the objects file, reads the data, and stores it in a
    dictionary.

    Args: None.

    Returns: objects: A dictionary where the keys are tuples of integers and
    the values are lists of strings.
    """
    # Open the file named "objects.txt" in read mode. This file contains the
    # data that we want to load.
    with open("objects.txt", "r", encoding="UTF-8") as object_file:
        # Initialize an empty dictionary. This will be used to store the data
        # from the file.
        objects = {}

        # Iterate over each line in the file. Each line represents a different
        # object.
        for line in object_file:
            # Split the line into components based on the tab character. The
            # first two components are converted to integers and used as keys
            # in the dictionary. The third component is the object name. The
            # rest of the components (if any) are stored as a list of values.
            key1, key2, obj_name, *value = line.strip().split('\t')

            # Store the data in the dictionary. The keys are tuples
            # consisting of two integers and the object name. The values are
            # lists of strings.
            objects[(int(key1), int(key2), obj_name)] = value

        # Close the file. This is important to free up system resources.
        object_file.close()

        # Return the dictionary containing the loaded data.
    return objects


def load_travel_table():
    """
    This function opens the travel table file, reads the data, and stores it
    in a dictionary.

    Args: None.

    Returns: travel_table: A dictionary where the keys are tuples of integers
    and the values are strings.
    """
    # Open the file named "travel_table.txt" in read mode
    with open("travel_table.txt", "r", encoding="UTF-8") as travel_file:
        # Initialize an empty dictionary to store the travel table data
        travel_table = {}

        # Iterate over each line in the file
        for line in travel_file:
            # Split the line into components based on the tab character The
            # first two components are converted to integers and used as keys
            # in the dictionary The rest of the components (if any) are
            # stored as a list of values
            key1, key2, *value = line.strip().split('\t')

            # Store the data in the dictionary The keys are tuples consisting of
            # two integers The values are strings obtained by joining all the
            # strings in `value` with a space
            travel_table[(int(key1), int(key2))] = ' '.join(value)

        # Close the file to free up system resources
        travel_file.close()

    # Return the dictionary containing the loaded data
    return travel_table


def print_instructions():
    """
    This function prints the instructions for the game from the
    instructions.txt file.

    Args: None.

    Returns: None.
    """
    # Open the file named "instructions.txt" in read mode
    with open("instructions.txt", "r", encoding="UTF-8") as file:

        # Read the entire content of the file and print it
        print(file.read())


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

    # if none of the conditions were met, return None
    return None


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
    """
    This function tests the functions load_game, load_objects,
    load_travel_table, and print_instructions.

    Args: None.

    Returns: None.
    """
    try:
        # Test the load_game function
        # Call the function and store its return value in the variable 'game'
        game = load_game()
        # Assert that 'game' is a dictionary
        assert isinstance(game, dict), "load_game() should return a dictionary"
        # Assert that 'game' is not empty
        assert len(game) > 0, "load_game() should return a non-empty dictionary"

        # Test the load_objects function
        # Call the function and store its return value in the variable 'objects'
        objects = load_objects()
        # Assert that 'objects' is a dictionary
        assert isinstance(objects,
                          dict), "load_objects() should return a dictionary"
        # Assert that 'objects' is not empty
        assert len(
            objects) > 0, ("load_objects()"
                           " should return a non-empty dictionary")

        # Test the load_travel_table function Call the function and store its
        # return value in the variable 'travel_table'
        travel_table = load_travel_table()
        # Assert that 'travel_table' is a dictionary
        assert isinstance(travel_table,
                          dict), ("load_travel_table()"
                                  " should return a dictionary")
        # Assert that 'travel_table' is not empty
        assert len(
            travel_table) > 0, ("load_travel_table() should"
                                " return a non-empty ""dictionary")

        # Test the print_instructions function
        # Since this function prints instructions and does not return anything,
        # we can only test if it runs without errors
        print_instructions()

        # If all the assertions pass, print a success message
        print("All tests passed successfully.")

    except AssertionError as error:
        # If any of the assertions fail, print an error message
        print(f"Test failed: {error}")


if __name__ == "__main__":
    main()
