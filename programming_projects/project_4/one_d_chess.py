def create_board():
    return ["WKi", "WKn", "WKn", "EMPTY", "EMPTY", "EMPTY", "BKn", "BKn", "BKi"]


def printable_board(board):
    # Replace "EMPTY" with "     "
    board = [cell if cell != "EMPTY" else "   " for cell in board]

    # Create the printable board
    printable = "+-----------------------------------------------------+\n"
    printable += "| {} | {} | {} | {} | {} | {} | {} | {} | {} |\n".format(*board)
    printable += "+-----------------------------------------------------+"

    return printable


def is_valid_move(board, position, player):
    if 0 <= position < len(board):
        if player == "WHITE" and board[position].startswith("W"):
            return True
        elif player == "BLACK" and board[position].startswith("B"):
            return True
    return False


def move_king(board, position, direction):
    if direction == "LEFT":
        new_position = position - 1
    else:
        new_position = position + 1
    while 0 <= new_position < len(board) and board[new_position] == "EMPTY":
        new_position += (1 if direction == "RIGHT" else -1)
    if 0 <= new_position < len(board):
        board[position], board[new_position] = "EMPTY", board[position]


def move_knight(board, position, direction):
    new_position = position + (2 if direction == "RIGHT" else -2)

    if 0 <= new_position < len(board):
        board[position], board[new_position] = "EMPTY", board[position]


def move(board, position, direction):
    if board[position].endswith("Ki"):
        move_king(board, position, direction)
    else:

        move_knight(board, position, direction)


def is_game_over(board):
    return "WKi" not in board or "BKi" not in board


def whos_the_winner(board):
    if "WKi" not in board:
        return "Black"
    elif "BKi" not in board:
        return "White"
    else:
        return None


def test_create_board():
    board = create_board()
    assert board == ["WKi", "WKn", "WKn", "EMPTY", "EMPTY", "EMPTY", "BKn", "BKn", "BKi"]


def test_printable_board():
    expected_output = """
    +-----------------------------------------------------+
    | WKi | WKn | WKn |     |     |     | BKn | BKn | BKi |
    +-----------------------------------------------------+
    """

    actual_output = printable_board(create_board())

    assert actual_output == expected_output, f"Expected: \n{expected_output}\nBut got: \n{actual_output}"


def test_is_valid_move():
    board = create_board()
    assert is_valid_move(board, 0, "WHITE") == True
    assert is_valid_move(board, 1, "BLACK") == False
    assert is_valid_move(board, 9, "BLACK") == False
    assert is_valid_move(board, -1, "BLACK") == False
    assert is_valid_move(board, 6, "BLACK") == True
    assert is_valid_move(board, 2, "WHITE") == False


def test_move_king():
    board = create_board()
    move_king(board, 0, "LEFT")
    assert board == ["EMPTY", "WKi", "WKn", "EMPTY", "EMPTY", "EMPTY", "BKn", "BKn", "BKi"]


def test_move_knight():
    board = create_board()
    move_knight(board, 1, "RIGHT")
    assert board == ["WKi", "EMPTY", "WKn", "WKn", "EMPTY", "EMPTY", "BKn", "BKn", "BKi"]


def test_is_game_over():
    board = create_board()
    assert is_game_over(board) == False


def test_whos_the_winner():
    board = create_board()
    assert whos_the_winner(board) is None


def main():
    # Run the test cases
    test_create_board()
    test_printable_board()
    test_is_valid_move()
    test_move_king()
    test_move_knight()
    test_is_game_over()
    test_whos_the_winner()

    print("All test cases passed.")


if __name__ == '__main__':
    main()
