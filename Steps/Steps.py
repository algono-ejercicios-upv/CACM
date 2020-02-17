def max_num(pos, arr_len):
    return min(pos, arr_len - pos)


def steps(x, y):
    end = abs(y - x)
    if end < 4:
        return end
    else:
        arr = [1] * end
        center_pos = end // 2

        arr_len = len(arr)
        if arr_len < 4:
            return arr_len

        if arr_len % 2 == 0:
            center_two = arr[center_pos:center_pos+2]
            if center_two[0] == 1 and center_two[1] == 1:
                arr = arr[0:center_pos] + [2] + arr[center_pos+2:]
            else:
                # TODO: Folding for centers > 1
                pass
        else:
            center = arr[center_pos]
            if center == 1:
                arr = arr[0:center_pos] + [2] + arr[center_pos+1:-1]
            else:
                # TODO: Folding for center > 1
                pass
        return arr_len


test_cases = int(input())
for test_case in range(test_cases):
    x_str, _, y_str = input().partition(' ')
    x, y = int(x_str), int(y_str)
    print(steps(x, y))
