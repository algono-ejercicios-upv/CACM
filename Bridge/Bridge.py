def get_best_bridge_strategy():
    # Get inputs
    number_of_people = int(input())

    # Remember: we sorted crossing_times, so the fastest is first, and the slowest last
    crossing_times = sorted([int(input()) for crossing_time_number in range(number_of_people)])
  
    # TODO: Call calculate_bridge_strategy for each possible strategy to calculate the one with minimal time, and print it with print_bridge_strategy
    print_bridge_strategy(*calculate_bridge_strategy(number_of_people, crossing_times))


def calculate_bridge_strategy(number_of_people: int, crossing_times: list):
    # Init relevant variables
    flashlight_crossed = False

    people_crossed = dict([(person, False) for person in crossing_times])

    time = 0
    steps = list()
    
    """
    TODO: Try a branch of the step graph, until exhausted
    (if no other steps are possible, except the same you did before, that branch was exhausted, and should be discarded)
    For any branch when you reached the end (all people have crossed), save it with its time
    If any better branch is found (less time), replace the last one with this one, but remember not to redo the other ones
    """
    all_people_have_crossed = False
    while not all_people_have_crossed:
        next_step = calculate_next_step_double(flashlight_crossed, people_crossed)
        if next_step:
            time, step = next_step
            first, second = step

            people_crossed[first] = 1
            people_crossed[second] = 1
            flashlight_crossed = not flashlight_crossed
        else:
            next_step = calculate_next_step_single(flashlight_crossed, people_crossed)
            if next_step:
                time, step = next_step
                person, _ = step

                people_crossed[person] = 1
                flashlight_crossed = not flashlight_crossed
            else:
                all_people_have_crossed = True
    
    return (time, steps)

def calculate_next_step_single(flashlight_crossed: bool, people_crossed: dict):
    time = 0
    step = None
    for person, crossed in people_crossed.items():
        if crossed == flashlight_crossed:
            time = person
            step = (person, None)
            break
    else:
        # All people have crossed; no further steps needed
        return None
    
    return (time, step)

def calculate_next_step_double(flashlight_crossed: bool, people_crossed: dict):
    step = list()
    for person, crossed in people_crossed.items():
        if len(step) == 2:
            break
        elif crossed == flashlight_crossed:
            step.append(person)
    else:
        # All people have crossed (or maybe all but one); no double-step possible
        return None
    
    return (max(step, default=0), tuple(step))

def print_bridge_strategy(time, steps):
    print(time)
    print(*[str.format("{0}{1}", first or "", f" {second}" if second else "") for first, second in steps], sep="\n", end="")


test_cases = int(input())
for test_case in range(test_cases):
    input() # Blank line between test cases (input)
    get_best_bridge_strategy()
    print() # Blank line between test cases (output)