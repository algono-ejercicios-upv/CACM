counting_dict = {1: 2, 2: 5, 3: 13}

def counting(number: int):
    if number < 1:
        return 0
    elif number < 4 or number in counting_dict:
        return counting_dict[number]
    else:
        res = 2*counting(number-1) + counting(number-2) + counting(number-3)
        counting_dict[number] = res
        return res

try:
    number_str = input()
    while number_str:
        number = int(number_str)
        print(counting(number))
        number_str = input()
except EOFError as err:
    pass