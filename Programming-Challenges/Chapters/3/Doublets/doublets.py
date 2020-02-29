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
    return str_diff(after, ref) - str_diff(before, ref)


def path_len(diff: int, inc: int):
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


def doublet_route(words: list, start: str, end: str):
    """
    Uses DFS to find the perfect minimal route.
    If no perfect route is found, it switches to BFS to find the minimal.

    Returns: Minimal doublet route between start and end
    """
    if start == end:
        return [start]
    else:
        diff = str_diff(start, end)
        if diff:
            doublets = [w for w in words if are_doublets(w, start)]
            min_path_word = min(doublets, key=str_diff_closure(end))
            next_diff = str_diff(min_path_word, end)

            if diff > next_diff:
                return [start] + doublet_route(words, min_path_word, end)
            else:
                return [start] + doublet_route_bfs(words, min_path_word, end)
        else:
            # Start and end must have the same length
            return None


def doublet_route_bfs(words: list, start: str, end: str):
    """
    Uses BFS to find the minimal route.

    Returns: Minimal doublet route between start and end
    """
    if start == end:
        return [start]
    else:
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
        route = doublet_route(words, word_one, word_two)
        print(*route, sep='\n') if route else print('No solution')
        pair = input()
except EOFError as err:
    pass
