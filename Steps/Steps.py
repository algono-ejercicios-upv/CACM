def steps(x, y):
    end = abs(y - x)
    if end < 4:
        return end
    else:
        actual_end = end - 2
        count = 1
        num = 1
        acc = 0
        while acc < actual_end:
            if num < ((count-1) // 2) + 2:
                num += 1
            else:
                count += 1
                acc += num
                num = 1
        return 2 + count

x = int(input("x: "))
y = int(input("y: "))

print(steps(x, y))