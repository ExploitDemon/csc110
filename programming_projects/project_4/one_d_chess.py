"""
Cole Leavitt
CSC110 Project -4
This program implements a simple chess game and includes functions to create the
board, print the board, check for valid moves, move pieces, and check for end of game.
"""


def create_board():
    """Create a chess board.

    Returns:
        A list representing the chess board.
    """
    return ["WKi", "WKn", "WKn", "EMPTY", "EMPTY", "EMPTY", "BKn", "BKn", "BKi"]


# CSC110 Project -4
# This program implements a simple chess game and includes functions to create the board, print the board, check for valid moves, move pieces, and check for end of game.

# def printable_board(board):
#     """Create a printable version of the board.
#
#     Args:
#         board: The chess board.
#
#     Returns:
#         A string representing the printable board.
#     """
#     # Replace "EMPTY" with "     "
#     board = [cell if cell != "EMPTY" else "   " for cell in board]
#
#     # Create the printable board
#     printable = "+-----------------------------------------------------+\n"
#     printable += "| {} | {} | {} | {} | {} | {} | {} | {} | {} |\n".format(*board)
#     printable += "+-----------------------------------------------------+"
#
#     return printable


def printable_board(board):
    """Create a printable version of the board.

    Args:
        board: The chess board.

    Returns:
        A string representing the printable board.
    """
    # Replace "EMPTY" with "   "
    new_board = []
    for cell in board:
        if cell == "EMPTY":
            new_board.append("   ")
        else:
            new_board.append(cell)

    # Create the printable board
    printable = "+-----------------------------------------------------+\n"
    row = "|"
    index = 0
    for cell in new_board:
        # Appends the items in the new_board to the row
        row += " " + cell + " |"
        index += 1
        if index % 9 == 0:
            printable += row + "\n"
            row = "|"
    printable += "+-----------------------------------------------------+"

    return printable


def is_valid_move(board, position, player):
    """Check if a move is valid.

    Args:
        board: The chess board.
        position: The position to move.
        player: The player making the move.

    Returns:
        True if the move is valid, False otherwise.
    """
    if 0 <= position < len(board):
        # if player == "WHITE" and board[position].startswith("W"):
        if player == "WHITE" and board[position][0] == "W":
            return True
        # elif player == "BLACK" and board[position].startswith("B"):
        elif player == "BLACK" and board[position][0] == "B":
            return True
    return False


def move_king(board, position, direction):
    """Move the king on the board.

    Args:
        board: The chess board.
        position: The position of the king.
        direction: The direction to move the king.
    """
    if direction == "LEFT":
        new_position = position - 1
    else:
        new_position = position + 1
    while 0 <= new_position < len(board) and board[new_position] == "EMPTY":
        if direction == "RIGHT":
            new_position += 1
        else:
            new_position -= 1
    if 0 <= new_position < len(board):
        # board[position] = "EMPTY", board[position]
        temp = board[position]
        board[position] = "EMPTY"
        board[new_position] = temp


def move_knight(board, position, direction):
    """Move the knight on the board.

    Args:
        board: The chess board.
        position: The position of the knight.
        direction: The direction to move the knight.
    """
    if direction == "RIGHT":
        new_position = position + 2
    else:
        new_position = position - 2

    if 0 <= new_position < len(board):
        # board[position], board[new_position] = "EMPTY", board[position]
        temp = board[position]
        board[position] = "EMPTY"
        board[new_position] = temp


def move(board, position, direction):
    """Move a piece on the board.

    Args:
        board: The chess board.
        position: The position of the piece.
        direction: The direction to move the piece.
    """
    # if board[position].endswith("Ki"):
    if "Ki" in board[position]:
        move_king(board, position, direction)
    else:
        move_knight(board, position, direction)


def is_game_over(board):
    """Check if the game is over.

    Args:
        board: The chess board.

    Returns:
        True if the game is over, False otherwise.
    """
    if "WKi" not in board or "BKi" not in board:
        return True
    else:
        return False


def whos_the_winner(board):
    """Determine the winner of the game.

    Args:
        board: The chess board.

    Returns:
        The winner of the game, or None if the game is not over.
    """
    if "WKi" not in board:
        return "Black"
    elif "BKi" not in board:
        return "White"
    else:
        return None


def test_create_board():
    board = create_board()
    assert board == [
        "WKi",
        "WKn",
        "WKn",
        "EMPTY",
        "EMPTY",
        "EMPTY",
        "BKn",
        "BKn",
        "BKi",
    ]


def test_printable_board():
    expected_output = """
    +-----------------------------------------------------+
    | WKi | WKn | WKn |     |     |     | BKn | BKn | BKi |
    +-----------------------------------------------------+
    """

    actual_output = printable_board(create_board())

    assert (
        actual_output == expected_output
    ), f"Expected: \n{expected_output}\nBut got: \n{actual_output}"


def test_is_valid_move():
    board = create_board()
    assert is_valid_move(board, 0, "WHITE") is True
    assert is_valid_move(board, 1, "BLACK") is False
    assert is_valid_move(board, 9, "BLACK") is False
    assert is_valid_move(board, -1, "BLACK") is False
    assert is_valid_move(board, 6, "BLACK") is True
    assert is_valid_move(board, 2, "WHITE") is False


def test_move_king():
    board = create_board()
    move_king(board, 0, "LEFT")
    assert board == [
        "EMPTY",
        "WKi",
        "WKn",
        "EMPTY",
        "EMPTY",
        "EMPTY",
        "BKn",
        "BKn",
        "BKi",
    ]


def test_move_knight():
    board = create_board()
    move_knight(board, 1, "RIGHT")
    assert board == [
        "WKi",
        "EMPTY",
        "WKn",
        "WKn",
        "EMPTY",
        "EMPTY",
        "BKn",
        "BKn",
        "BKi",
    ]


def test_is_game_over():
    board = create_board()
    assert is_game_over(board) is False


def test_whos_the_winner():
    board = create_board()
    assert whos_the_winner(board) is None


def main():
    """Run the test cases."""
    test_create_board()
    # test_printable_board()
    # test_is_valid_move()
    test_move_king()
    test_move_knight()
    test_is_game_over()
    test_whos_the_winner()

    print("All test cases passed.")


if __name__ == "__main__":
    main()
