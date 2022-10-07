import string

# Build base36 list
BASE_36 = [str(value) for value in range(10)]
BASE_36.extend(string.ascii_uppercase)


def decimal_to_base36(n: int) -> str:
    """
    Converts a decimal value to a base 36 notation
    """
    if n >= 36:
        return "-"
    return BASE_36[n]


def base36_to_decimal(n: str) -> int:
    """
    Converts a base 36 value to decimal notation
    """
    if not (n in BASE_36):
        return -1
    return BASE_36.index(n)


def get_drawable_board(
    board_state: str, empty_char="⬛", queen_char="♟"
) -> list:
    """
    Populates a chess board represented as a bidimensional list
    given a board_state string containing base36 encoded values
    """
    # initialize board
    result = [[empty_char] * len(board_state) for _ in range(len(board_state))]

    # place queens according to input string
    for row_index, queen_position in enumerate(board_state):
        result[row_index][base36_to_decimal(queen_position)] = queen_char
    return result


def get_queens(n: int) -> set:
    queens = set()
    board_state = ""

    # avoid calculations greater than base36 string parsing capability
    if n > len(BASE_36):
        return queens

    # Placement constraints
    used_cols = set()
    used_diagonals_up = set()
    used_diagonals_down = set()

    def backtrack(row, board_state):
        if row == n:
            queens.add(board_state)
            return
        
        for column in range(n):
            if ( # Space ain't available
                (column in used_cols)
                or ((row + column) in used_diagonals_up)
                or ((row - column) in used_diagonals_down)
            ):
                continue

            # Place queen
            used_cols.add(column)
            used_diagonals_up.add(row + column)
            used_diagonals_down.add(row - column)
            board_state += decimal_to_base36(column)

            backtrack(row + 1, board_state)

            # Remove queen
            used_cols.remove(column)
            used_diagonals_up.remove(row + column)
            used_diagonals_down.remove(row - column)
            board_state = board_state[:-1]

    backtrack(0, board_state)
    return queens
