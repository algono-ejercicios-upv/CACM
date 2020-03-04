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


def are_doublets(one: str, two: str):
    if len(one) == len(two):
        for index, (l_one, l_two) in enumerate(zip(one, two)):
            if l_one != l_two:
                return one[index+1:] == two[index+1:] if index < len(one) - 1 else True
        else:
            return False
    else:
        return False


def check_base(words: list, start: str, end: str, **kwargs):
    """
    kwargs:
    - max_len: max length of route to be considered valid
    - func: function called after checking the base (args passed: words, start, end)
    - visited = list of visited words (so that we don't visit them again)
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
                if diff >= max_len - 1:
                    return None
                elif diff == max_len - 2:
                    return ([start, end], 0) if are_doublets(start, end) else None

            func, visited = kwargs['func'], kwargs['visited']
            return func(words, start, end, visited=visited) if func else None
        else:
            return None  # Start and end must have the same length


def doublet_route_dfs(words: list, start: str, end: str, max_len=None, visited=None):
    """
    Uses DFS to find the perfect minimal route.
    If no perfect route is found, it switches to BFS to find the minimal.

    Returns: Tuple (route, inc) minimal
    """
    return check_base(words, start, end, max_len=max_len, func=doublet_route_dfs_impl, visited=visited)


def doublet_route_dfs_impl(words: list, start: str, end: str, **kwargs):
    """
    kwargs:
    - visited = list of visited words (so that we don't visit them again)
    """
    visited: set = kwargs['visited']
    doublets = sorted([w for w in words if (visited == None or w not in visited)
                       and are_doublets(w, start)], key=str_diff_closure(end))
    res = min_len = None
    for min_path_word in doublets:
        actual_inc = str_inc(end, start, min_path_word)
        if actual_inc < 0:
            inc = actual_inc if actual_inc > 0 else 0

            visited = set(visited).union(start) if visited else set([start])
            next_res = doublet_route_dfs(
                words, min_path_word, end, max_len=min_len, visited=visited)
            if next_res:
                next_route, next_inc = next_res
                route = [start] + next_route
                inc += next_inc
                if inc == 0:
                    return (route, inc)
                else:
                    res = (route, inc)
                    min_len = len(route)
            else:
                return res
    else:
        return doublet_route_bfs(words, start, end)


def doublet_route_bfs(words: list, start: str, end: str, max_len=None, visited=None):
    """
    Uses BFS to find the minimal route.

    Returns: Minimal doublet route between start and end
    """
    return check_base(words, start, end, max_len=max_len, func=doublet_route_bfs_impl, visited=visited)


def doublet_route_bfs_impl(words: list, start: str, end: str, **kwargs):
    """
    kwargs:
    - visited = list of visited words (so that we don't visit them again)
    """
    next_results = [([start], 0)]
    next_words = [[]]

    visited: set = kwargs['visited']

    res = min_len = None

    for word in words:
        if are_doublets(start, word):
            if word == end:
                return [start, end]
            else:
                next_words[0].append(word)

    visited = set(visited).union(start) if visited else set([start])

    current_len = 0
    while len(visited) < len(words) and len(next_results) > 0 and (min_len == None or current_len < min_len - 1):
        results, current_words = next_results, next_words
        next_results, next_words = list(), list()

        for index, (route, inc) in enumerate(results):
            for word in current_words[index]:
                if word not in visited:
                    if word == end:
                        route.append(word)
                        return (route, inc)
                    else:
                        actual_word_inc = str_inc(end, route[-1], word)
                        word_inc = actual_word_inc if actual_word_inc > 0 else 0
                        acc_inc = inc + word_inc

                        visited.add(word)

                        if actual_word_inc < 0:
                            res = doublet_route_dfs(
                                words, word, end, max_len=min_len, visited=visited)
                            if res:
                                res_route, res_inc = res
                                res_route = route + res_route
                                res_inc += acc_inc
                                res = (res_route, res_inc)
                                min_len = len(res_route)
                        else:
                            word_route = route.copy()
                            word_route.append(word)

                            word_doublets = [
                                w for w in words if w not in visited and are_doublets(w, word)]

                            if len(word_doublets) > 0:
                                next_results.append(
                                    (word_route, acc_inc))
                                next_words.append(word_doublets)

        current_len += 1
    else:
        return res


def debug():
    words = ['hola',
             'bola',
             'cola',
             'mola',
             'mala',
             'bala',
             'sala',
             'sota',
             'cota',
             'bota',
             'rota']

    pairs = [('hola', 'rota'),
             ('sala', 'sota')]
    
    started = False
    for pair in pairs:
        if started:
            print()  # Empty line between cases
        else:
            started = True

        word_one, word_two = pair
        res = doublet_route_dfs(words, word_one, word_two)
        if res:
            route, inc = res
            print(*route, sep='\n')
        else:
            print('No solution')


def main():
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

main()