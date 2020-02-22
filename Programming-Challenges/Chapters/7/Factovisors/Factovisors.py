def is_factovisor(n, m):
    if m < n:
        return True


def str_factovisor(n, m, is_factovisor):
    return str.format("{0} {1} {2}!",
                      m,
                      "divides" if is_factovisor else "does not divide",
                      n)


try:
    numbers_str = input()
    while numbers_str:
        n_str, _, m_str = numbers_str.partition(' ')
        n, m = int(n_str), int(m_str)
        print(str_factovisor(n, m, is_factovisor(n, m)))
        numbers_str = input()
except EOFError as err:
    pass
