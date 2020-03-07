def is_reachable(automaton_state, number_of_cells, evolution_rules):
    return is_reachable_impl(automaton_state, number_of_cells, evolution_rules, 0, None, None)


def is_reachable_impl(automaton_state, number_of_cells, evolution_rules, cell_pos, first_full_cell_state, last_full_cell_state):
    if cell_pos == number_of_cells-1:
        return first_full_cell_state[-2:] == last_full_cell_state[:2]
    else:
        cell_state = automaton_state[cell_pos]

        for full_cell_state in evolution_rules[cell_state]:
            # It is only valid if the first two digits of it match the last one's last two
            if last_full_cell_state == None or last_full_cell_state[-2:] == full_cell_state[:2]:
                res = is_reachable_impl(automaton_state, number_of_cells, evolution_rules, cell_pos+1,
                                        full_cell_state if first_full_cell_state == None else first_full_cell_state, full_cell_state)
                if res:
                    return res
        else:
            return False


# Every possible rule input (L-C-R) (0-0-0 -> 1-1-1)
rule_inputs = [
    '000',
    '001',
    '010',
    '011',
    '100',
    '101',
    '110',
    '111'
]


try:
    automaton_str = input()
    while automaton_str:
        automaton_params = automaton_str.split(' ')

        automaton_id, number_of_cells, automaton_state = int(automaton_params[0]), int(
            automaton_params[1]), automaton_params[2]

        evolution_rules = {'0': [], '1': []}  # All possible states for a cell

        automaton_id_left = automaton_id
        # For every possible rule input
        for rule in rule_inputs:
            # Calculate the state it generates (from the automaton id)
            out_state = str(automaton_id_left % 2)
            # Take out the state from the id
            automaton_id_left //= 2
            # Store into a list of which rules generate that state
            evolution_rules[out_state].append(rule)

        print('REACHABLE' if is_reachable(automaton_state, number_of_cells,
                                          evolution_rules) else 'GARDEN OF EDEN')

        automaton_str = input()
except EOFError as err:
    pass
