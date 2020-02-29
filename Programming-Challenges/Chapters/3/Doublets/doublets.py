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
            return ["No solution."]


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
        print(*doublet_route(words, word_one, word_two), sep='\n')
        pair = input()
except EOFError as err:
    pass
