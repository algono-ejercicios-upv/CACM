def get_best_bridge_strategy():
    # Get inputs
    number_of_people = int(input())

    # Remember: we sorted crossing_times, so the fastest is first, and the slowest last
    crossing_times = sorted([int(input()) for crossing_time_number in range(number_of_people)])
  
    # TODO: Call calculate_bridge_strategy for each possible strategy to calculate the one with minimal time, and print it with print_bridge_strategy
    # print_bridge_strategy(*calculate_bridge_strategy(number_of_people, crossing_times))

"""
    TODO: Functions for both possible strategies
    Strategy 1:
        - Two fastest cross
        - The fastest between them crosses back
        - Two slowest cross
        - Second fastest crosses back
        - Repeat until finished
    
    Strategy 2:
        - Fastest and slowest cross
        - Fastest crosses back
        - Repeat until finished
"""

"""
    TODO: Function for deciding which strategy fits best
"""

def print_bridge_strategy(time, steps):
    print(time)
    print(*[str.format("{0}{1}", first or "", f" {second}" if second else "") for first, second in steps], sep="\n", end="")


test_cases = int(input())
for test_case in range(test_cases):
    input() # Blank line between test cases (input)
    get_best_bridge_strategy()
    print() # Blank line between test cases (output)