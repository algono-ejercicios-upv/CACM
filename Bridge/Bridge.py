def calculate_bridge_strategy():
    # Get inputs
    number_of_people = int(input())
    crossing_times = [int(input()) for crossing_time_number in range(number_of_people)]
    crossing_times.sort()

    print(crossing_times)
    # Init relevant variables
    flashlight_crossed = False
    people_crossed = [False] * number_of_people
    
    # We sorted crossing_times, so the fastest is first, and the slowest last
    # TODO: Calculate the minimal time, and print it with the steps required
    



test_cases = int(input())
for test_case in range(test_cases):
    input() # Blank line between test cases (input)
    calculate_bridge_strategy()
    print() # Blank line between test cases (output)