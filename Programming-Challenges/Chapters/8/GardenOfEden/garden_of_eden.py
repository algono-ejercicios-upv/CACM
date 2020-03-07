def bin_format(n, leading_zeros=0):
    return n[2:].zfill(leading_zeros)


def full_cell_state_match(one, two):
    return one[-2:] == two[:2]


def is_reachable(automaton_state, evolution_rules):
    return is_reachable_impl(automaton_state, evolution_rules, 0, None, None)


def is_reachable_impl(automaton_state, evolution_rules, cell_pos, first_full_cell_state, last_full_cell_state):
    if cell_pos == len(automaton_state):
        return first_full_cell_state == last_full_cell_state
    else:
        cell_state = automaton_state[cell_pos]

        for full_cell_state in evolution_rules[cell_state]:
            if last_full_cell_state == None or full_cell_state_match(last_full_cell_state, full_cell_state):
                res = is_reachable_impl(automaton_state, evolution_rules, cell_pos+1,
                                        full_cell_state if first_full_cell_state == None else first_full_cell_state, full_cell_state)
                if res:
                    return res
        else:
            return False


try:
    automaton_str = input()
    while automaton_str:
        automaton_params = automaton_str.split(' ')

        automaton_id, number_of_cells, automaton_state = int(automaton_params[0]), int(
            automaton_params[1]), automaton_params[2]

        automaton_rule_states = bin_format(bin(automaton_id), 8)

        evolution_rules = {'0': [], '1': []}  # All possible states for a cell

        # For every rule (L-C-R) (0-0-0 -> 1-1-1) as an int (0 -> 7), and the state it generates ('new_state')
        for rule_int, new_state in zip(range(8), reversed(automaton_rule_states)):
            # Get a string representation of it
            rule = bin_format(bin(rule_int), 3)

            # Store into a list of which rules generate that state
            evolution_rules[new_state].append(rule)

        print('REACHABLE' if is_reachable(automaton_state,
                                          evolution_rules) else 'GARDEN OF EDEN')

        automaton_str = input()
except EOFError as err:
    pass
