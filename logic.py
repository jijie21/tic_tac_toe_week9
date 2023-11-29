def check_winner(board):
    # check rows
    for row in board:
        if len(set(row)) == 1 and row[0] is not None:
            return row[0]

    # check columns
    for i in range(len(board)):
        column = [board[j][i] for j in range(len(board))]
        if len(set(column)) == 1 and column[0] is not None:
            return column[0]

    # check diagonals
    top_left_to_bottom_right = [board[i][i] for i in range(len(board))]
    if len(set(top_left_to_bottom_right)) == 1 and top_left_to_bottom_right[0] is not None:
        return top_left_to_bottom_right[0]

    top_right_to_bottom_left = [board[i][len(board)-i-1] for i in range(len(board))]
    if len(set(top_right_to_bottom_left)) == 1 and top_right_to_bottom_left[0] is not None:
        return top_right_to_bottom_left[0]

    # check for draw
    flat_board = [cell for row in board for cell in row]

    if None not in flat_board:
        return "Draw"

    return None

def get_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

def print_board(board):
    for row in board:
        print(row)


def get_player_input(current_player, player_move=None):
    if player_move is not None:
        return player_move

    prompt = f"Player {current_player} > \n "
    player_input = input(prompt)

    row_col_list = player_input.split(',')
    row, col = [int(x) for x in row_col_list]

    return row, col


def switch_player(current_player):
    if current_player == "X":
        return "O"
    return "X"
