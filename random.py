"""
Tristen Porter
CSC110 Project-4
<>
"""


def create_board():
    """ Create Chess Board"""
    print(['WKi', 'WKn', 'WKn', 'EMPTY', 'EMPTY', 'BKn', 'BKn', 'BKi'])


board = create_board


def printable_board(predetermined_board):
    """
    Create a board that is visible
 
    Args:
         predetermined_board: The chess board.
 
     Returns:
         The board that is a
         string representing the board
    """
    new_board = []

    # Replace "EMPTY" str to "   " str
    for cell in predetermined_board:
        if cell == "EMPTY":
            new_board.append("   ")
        else:
            new_board.append(cell)

    # Create New board
    new_board_str = "+-----------------------------------------------------+\n"
    row = "|"
    index = 0
    for cell in new_board:
        row = " " + cell + " |"
        index += 1
        if index % 9 == 0:
            new_board_str += row + "\n"
            row = "|"
        new_board_str += "+-----------------------------------------------------+"

    return new_board_str


# def is_valid_move(board,position,player):


expected_output = """
+-----------------------------------------------------+
| WKi | WKn  | WKn |     |     |     | BKn | BKn | BKi |
+-----------------------------------------------------+
"""
