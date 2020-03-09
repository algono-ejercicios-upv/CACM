N_RULES = 8


def is_reachable(cell_pos, curr_state):
    if cell_pos == n-1:
        return ((curr_state >> 1) & 1) == ((first >> 2) & 1) and (curr_state & 1) == ((first >> 1) & 1)
    else:
        visited[cell_pos*curr_state] = True
        for i in range(N_RULES):
            if ((a_id >> i) & 1) == int(a_state[cell_pos]) and ((curr_state >> 1) & 1) == ((i >> 2) & 1) and (curr_state & 1) == ((i >> 1) & 1):
                if not visited[cell_pos+1 * curr_state] and is_reachable(cell_pos+1, i):
                    return True
        else:
            return False


try:
    a_str = input()
    while a_str:
        a_params = a_str.split(' ')

        a_id, n, a_state = int(a_params[0]), int(
            a_params[1]), a_params[2]

        reachable = False
        for i in range(N_RULES):
            if ((a_id >> i) & 1) == int(a_state[0]):
                visited, first = bytearray(n * N_RULES), i
                reachable = is_reachable(0, i)

                if reachable:
                    break

        print('REACHABLE' if reachable else 'GARDEN OF EDEN')

        a_str = input()
except EOFError as err:
    pass
