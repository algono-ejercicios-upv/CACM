
def int_to_bin_str(n, leading_zeros=0):
    return bin(n)[2:].zfill(leading_zeros)


try:
    automaton_str = input()
    while automaton_str:
        automaton_params = automaton_str.split(' ')

        automaton_id, cell_number, init_state = int(automaton_params[0]), int(
            automaton_params[1]), int(automaton_params[2])

        automaton_new_states = int_to_bin_str(automaton_id, 8)

        evolution_rules = dict()

        # For every possible state (L-C-R) (0-0-0 -> 1-1-1)
        for state_int, new_state in zip(range(8), reversed(automaton_new_states)):
            state = int_to_bin_str(state_int, 3)
            # Match the state to the new one (defined by the automaton id in binary)
            evolution_rules[state] = new_state

        """
        For now, we print the rules
        TODO: Make algorithm to decide if a state is REACHABLE or GARDEN OF EDEN
        """
        print(evolution_rules)

        automaton_str = input()
except EOFError as err:
    pass
