def gcd(a, b):
    """
    Returns: (X, Y, D)
    from a*X + b*Y = D
    D = gcd(a,b)
    """
    if b > a:
        return gcd(b, a)
    if b == 0:
        return (1, 0, a)
    
    x1, y1, d = gcd(b, a % b)
    x = y1
    y = (x1 - (a/b)*y1)
    return (x, y, d)

try:
    numbers_str = input()
    while numbers_str:
        a_str, _, b_str = numbers_str.partition(' ')
        a, b = int(a_str), int(b_str)
        print(*gcd(a, b), sep=' ')
        numbers_str = input()
except EOFError as err:
    pass