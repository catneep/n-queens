def get_queens(n: int):
    queens = []
    board = [['.'] * n for _ in range(n)]

    # Placement constraints
    used_cols = set()
    used_diagonals_up = set()
    used_diagonals_down = set()

    def backtrack(row):
        if row == n:
            copy = ['.'.join(row) for row in board]
            queens.append(copy)
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
            board[row][column] = '♟'

            backtrack(row + 1)

            # Remove queen
            used_cols.remove(column)
            used_diagonals_up.remove(row + column)
            used_diagonals_down.remove(row - column)
            board[row][column] = '.'

    backtrack(0)
    return queens
