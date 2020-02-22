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
            while top > 1 and left > top:
                times = left // top
                count += times
                extra = top * times
                total += extra
                left -= extra
                top -= 1
            if top > 1 and left > 0:
                return count + 1  # left 1 time
            else:
                return count + left  # 1s left times


test_cases = int(input())
for test_case in range(test_cases):
    x_str, _, y_str = input().partition(' ')
    x, y = int(x_str), int(y_str)
    print(steps(x, y))
