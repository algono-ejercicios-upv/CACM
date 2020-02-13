"""
Strategies one and two are only aplicable when len(people) > 3
"""


def time_apply_strategy_one(A, B, C, D):
    return A + 2*B + D


def steps_apply_strategy_one(A, B, C, D):
    return [(A, B), (A, None), (C, D), (B, None)]


def time_apply_strategy_two(A, B, C, D):
    return 2*A + C + D


def steps_apply_strategy_two(A, B, C, D):
    return [(A, D), (A, None), (A, C), (A, None)]


def apply_best_strategy_len_gt_three(relevant_people: list):
    T_one = time_apply_strategy_one(*relevant_people)
    T_two = time_apply_strategy_two(*relevant_people)

    if T_two < T_one:
        T = T_two
        P = steps_apply_strategy_two(*relevant_people)
    else:
        T = T_one
        P = steps_apply_strategy_one(*relevant_people)

    return (T, P)


"""
Strategies when len(people) is 1, 2 or 3
"""


def apply_strategy_len_three(A, B, D):
    T = A + B + D
    P = [(A, D), (A, None), (A, B)]
    return (T, P)


def apply_strategy_len_two(A, D):
    T = D
    P = [(A, D)]
    return (T, P)


def apply_strategy_len_one(person):
    T = person
    P = [(person, None)]
    return (T, P)


def get_best_bridge_strategy(people: list):
    arr = people.copy()
    T = 0
    P = []
    while len(arr) > 0:
        if len(arr) > 3:
            next_T, next_P = apply_best_strategy_len_gt_three(
                (arr[0], arr[1], arr[-2], arr[-1]))  # A, B, C, D
            arr = arr[:-2]
        else:
            if len(arr) == 3:
                next_T, next_P = apply_strategy_len_three(
                    arr[0], arr[1], arr[-1])  # A, B, D
            elif len(arr) == 2:
                next_T, next_P = apply_strategy_len_two(
                    arr[0], arr[-1])  # A, D
            else:
                next_T, next_P = apply_strategy_len_one(arr[0])
            # These are last steps, in all cases all people crossed
            arr.clear()

        T += next_T
        P += next_P

    return (T, P)


def get_best_bridge_strategy_from_input():
    # Get inputs
    number_of_people = int(input())

    # Remember: we sorted people, so the fastest is first, and the slowest last
    people = sorted([int(input())
                     for _ in range(number_of_people)])

    print_bridge_strategy(*get_best_bridge_strategy(people))


def print_bridge_strategy(time: int, steps: list):
    print(time)
    print(*[str.format("{0}{1}", first or "", f" {second}" if second else "")
            for first, second in steps], sep="\n")


test_cases = int(input())
for test_case in range(test_cases):
    input()  # Blank line between test cases (input)
    get_best_bridge_strategy_from_input()

    if test_case < test_cases - 1:
        print()  # Blank line between test cases (output)
