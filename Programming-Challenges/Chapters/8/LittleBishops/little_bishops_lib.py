"""
Create an n*n matrix (board)
Assign -1 when placing a bishop, and add 1 to each spot in its diagonal
Assign only if the spot has a 0, use recursion, and undo the placing
to make backtracking

Example of a solved state (n=3, k=3):
[
    [ -1 , 1 ,  1],
    [  0 , 1 , -1],
    [ -1 , 1 ,  1]
]

Count these states, and return the total
"""


def apply_to_diagonals_from(matrix: list, mat_len: int, row: int, column: int, func):
    # upper left
    r_aux, c_aux = row-1, column-1
    while r_aux >= 0 and c_aux >= 0:
        func(matrix, r_aux, c_aux)
        r_aux -= 1
        c_aux -= 1

    # upper right
    r_aux, c_aux = row+1, column-1
    while r_aux < mat_len and c_aux >= 0:
        func(matrix, r_aux, c_aux)
        r_aux += 1
        c_aux -= 1

    # lower left
    r_aux, c_aux = row-1, column+1
    while r_aux >= 0 and c_aux < mat_len:
        func(matrix, r_aux, c_aux)
        r_aux -= 1
        c_aux += 1

    # lower right
    r_aux, c_aux = row+1, column+1
    while r_aux < mat_len and c_aux < mat_len:
        func(matrix, r_aux, c_aux)
        r_aux += 1
        c_aux += 1


def mark(board, r, c):
    spot = board[r][c]
    if spot >= 0:
        board[r][c] += 1


def undo(board, r, c):
    spot = board[r][c]
    if spot >= 0:
        board[r][c] -= 1


def get_state_from_board(board, n):
    return sorted([n*r+c for r, row in enumerate(board) for c, spot in enumerate(row) if spot == -1])


def little_bishops_from(board, n, k, visited_states=[]):
    current_state = get_state_from_board(board, n)
    #print(f"{current_state} || {visited_states}")
    if current_state in visited_states:
        return 0
    else:
        visited_states.append(current_state)

        if k == 0:
            #print(board)
            return 1

        total = 0
        for r, row in enumerate(board):
            for c, spot in enumerate(row):
                if spot == 0:
                    board[r][c] = -1
                    apply_to_diagonals_from(board, n, r, c, mark)

                    total += little_bishops_from(board, n, k-1, visited_states)

                    apply_to_diagonals_from(board, n, r, c, undo)
                    board[r][c] = spot

        return total


def little_bishops(n, k):
    board = [([0] * n) for i in range(n)]
    return little_bishops_from(board, n, k)


def list_str(res_dict):
    return '[\n ' + str(str(res_dict)[1:-1].replace(', [', ',\n [')) + '\n]'


def dict_str(res_dict):
    return '{\n ' + str(str(res_dict)[1:-1].replace(', (', ',\n (')) + '\n}'


res_dict = dict()
n, k = int(input("n: ")), int(input("k: ")) 
res = little_bishops(n, k)
print(res)

#res_dict[(n, k)] = res
#print(f'res_str = {dict_str(res_dict)}')
