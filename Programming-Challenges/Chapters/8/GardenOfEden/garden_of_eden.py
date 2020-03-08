N_RULES = 8


def is_reachable(n, rules, cell_pos, origin, target):
    if cell_pos == n-1:
        s_last = (origin[n-2] << 2) | (origin[n-1] << 1) | (origin[0] << 0)
        s_first = (origin[n-1] << 2) | (origin[0] << 1) | (origin[1] << 0)
        return target[cell_pos] == rules[s_last] and target[0] == rules[s_first]
    else:
        for i in range(N_RULES):
            if rules[i] == target[cell_pos] and ((i >> 2) & 1) == origin[cell_pos-1] and ((i >> 1) & 1) == origin[cell_pos]:
                res = is_reachable(n, rules,
                                   cell_pos+1, origin + [(i >> 0) & 1], target)
                if res:
                    return res
        else:
            return False


try:
    a_str = input()
    while a_str:
        a_params = a_str.split(' ')

        a_id, n, a_state = int(a_params[0]), int(
            a_params[1]), a_params[2]

        target = [int(s) for s in a_state]

        rules = [(a_id >> i) & 1 for i in range(N_RULES)]

        reachable = False
        for i in range(N_RULES):
            if rules[i] == target[0]:
                origin = [(i >> 1) & 1, (i >> 0) & 1]

                reachable = is_reachable(n, rules, 1, origin, target)

                if reachable:
                    break

        print('REACHABLE' if reachable else 'GARDEN OF EDEN')

        a_str = input()
except EOFError as err:
    pass
