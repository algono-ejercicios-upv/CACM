def str_diff(one: str, two: str):
    if len(one) == len(two):
        diff = 0
        for l_one, l_two in zip(one, two):
            if l_one != l_two:
                diff += 1
        return diff
    else:
        return None


def str_diff_closure(one: str):
    return lambda two: str_diff(one, two)


def str_inc(ref: str, before: str, after: str):
    actual_inc = str_diff(after, ref) - str_diff(before, ref)
    return actual_inc if actual_inc > 0 else 0


def route_len(diff: int, inc: int):
    return 2*inc + diff


def are_doublets(one: str, two: str):
    if len(one) == len(two):
        diff = 0
        for l_one, l_two in zip(one, two):
            if l_one != l_two:
                diff += 1
            if diff > 1:
                return False

        return diff == 1
    else:
        return False


def check_base(words: list, start: str, end: str, **kwargs):
    """
    kwargs:
    - max_len: max length of route to be considered valid
    - func: function called after checking the base (args passed: words, start, end)
    """
    if len(words) == 0:
        return None
    elif start == end:
        return ([start], 0)
    else:
        diff = str_diff(start, end)
        if diff:
            max_len = kwargs['max_len']
            if max_len:
                if diff >= max_len:
                    return None
                elif diff == max_len - 2:
                    return ([start, end], 0) if are_doublets(start, end) else None

            func = kwargs['func']
            return func(words, start, end) if func else None
        else:
            return None  # Start and end must have the same length


def doublet_route_dfs(words: list, start: str, end: str, max_len=None):
    """
    Uses DFS to find the perfect minimal route.
    If no perfect route is found, it switches to BFS to find the minimal.

    Returns: Tuple (route, inc) minimal
    """
    return check_base(words, start, end, max_len=max_len, func=doublet_route_dfs_impl)


def doublet_route_dfs_impl(words: list, start: str, end: str):
    doublets = [w for w in words if are_doublets(w, start)]
    min_path_word = min(doublets, key=str_diff_closure(end))
    inc = str_inc(end, start, min_path_word)
    if inc == 0:
        res = doublet_route_dfs([w for w in words if w != start], min_path_word, end)
        if res:
            next_route, next_inc = res
            route = [start] + next_route
            inc += next_inc
            if inc == 0:
                return (route, inc)
            else:
                min_res = (route, inc)
                min_len = route_len(str_diff(start, end), inc)
                res = doublet_route_dfs([w for w in words if w != start], min_path_word, end, max_len=min_len)
                
                while res:
                    next_route, next_inc = res
                    route = [start] + next_route
                    inc += next_inc
                    min_res = (route, inc)
                    min_len = route_len(str_diff(start, end), inc)
                    res = doublet_route_dfs([w for w in words if w != start], min_path_word, end, max_len=min_len)
                
                return min_res
        else:
            return res
    else:
        return doublet_route_bfs(words, start, end)


def doublet_route_bfs(words: list, start: str, end: str, max_len=None):
    """
    Uses BFS to find the minimal route.

    Returns: Minimal doublet route between start and end
    """
    return check_base(words, start, end, max_len=max_len, func=doublet_route_bfs_impl)


def doublet_route_bfs_impl(words: list, start: str, end: str):
    next_routes = [[start]]
    next_words = [[]]

    remaining_words = [w for w in words if w != start]

    for word in words:
        if are_doublets(start, word):
            if word == end:
                return [start, end]
            else:
                next_words[0].append(word)

    while len(remaining_words) > 0 and len(next_routes) > 0:
        routes, current_words = next_routes, next_words
        next_routes, next_words = list(), list()

        for index, route in enumerate(routes):
            for word in current_words[index]:
                if word in remaining_words:
                    if word == end:
                        route.append(word)
                        return route
                    else:
                        word_route = route.copy()
                        word_route.append(word)

                        remaining_words.remove(word)

                        word_doublets = [
                            w for w in remaining_words if are_doublets(w, word)]

                        if len(word_doublets) > 0:
                            next_routes.append(word_route)
                            next_words.append(word_doublets)
    else:
        return None


try:
    word = input()
    words = []
    while word:
        words.append(word)
        word = input()

    pair = input()
    started = False
    while pair:
        if started:
            print()  # Empty line between cases
        else:
            started = True

        word_one, _, word_two = pair.partition(' ')
        res = doublet_route_dfs(words, word_one, word_two)
        if res:
            route, inc = res
            print(*route, sep='\n')
        else:
            print('No solution')
        
        pair = input()
except EOFError as err:
    pass
