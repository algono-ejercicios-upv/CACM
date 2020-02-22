def ones(n: int):
    counter = 0
    x = n
    while x > 0:
        while (x % 10) == 1:
            counter += 1
            x //= 10
        if x > 0:
            x += n
    print(counter)

try:
    while True:
        ones(int(input()))
except EOFError as err:
    pass
