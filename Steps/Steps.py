def steps(x, y):
    end = abs(y - x)
    if end < 4:
        return end
    else:
        top = end ** (1/2)
        top_int = int(top)
        count = 2*top_int-1
        if top % 1 == 0:
            return count
        else:
            total = int(top_int**2)
            top = top_int
            left = end - total
            if left > top:
                min_times = left // top
                if min_times < left:
                    """
                    TODO: Fix this trying the other cases mentioned.

                    Explanation:

                    When end = 23, the extra (min steps) is (3, 3, 1)
                    We are only trying combinations of the same number
                    (i.e.: (1, 1, 1), (2, 2, 2), etc.)
                    But not cases like this.
                    """
                    for times in range(min_times, left):
                        num = left / times
                        if num % 1 == 0 and num < top:
                            return count + times
                return count + left  # 1s left times
            else:
                return count + 1  # left 1 time


test_cases = int(input())
for test_case in range(test_cases):
    x_str, _, y_str = input().partition(' ')
    x, y = int(x_str), int(y_str)
    print(steps(x, y))
