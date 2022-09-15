from datetime import datetime, timedelta

from Tools.DB import get_default_engine, create_model, add_solution
from Models.Solution import Solution
from Logic.Queens import get_queens

MAX_ITERATIONS: int = 17 # Wont get past this point within 10 minutes
SHOW_BOARD: bool = False

def print_solutions(n: int, board= False) -> None:
    """
    Outputs a representation of a given board state
    """
    results = get_queens(n)
    print(f'Total solutions found for {n}x{n}:', len(results))

    if not board: return # else output full board

    for solution in results:
        [print(row) for row in solution]
        print('_'*32)

def get_solution(n: int) -> Solution:
    current_solution = Solution(method= 'backtrack', n_queens= n)
    print(f'{n} queens\n')

    result = len(get_queens(n))

    current_solution.update_total(result)

    return current_solution

if __name__ == "__main__":
    print('Testing DB')
    try:
        engine = get_default_engine()
        print('DB Connection was successful!')
    except Exception as e:
        print('DB Error', e)
        exit(1)

    create_model()
    total_time = timedelta(seconds= 0)

    print('Gettings results...')
    for n in range(8, MAX_ITERATIONS):
        starting_time = datetime.now()

        solution = get_solution(n)
        add_solution(solution)

        total_time += (datetime.now() - starting_time)
    
    print('Total execution time:', total_time)
