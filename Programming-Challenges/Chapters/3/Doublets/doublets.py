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


def get_doublets(words: list, word: str, visited=None):
    doublets = set()
    for i, ac in enumerate(word):
        for ci in range(ord('a'), ord('z')+1):
            c = chr(ci)
            if c != ac:
                if len(word) == 1:
                    doublet = c
                elif i == 0:
                    doublet = c + word[1:]
                elif i == len(word)-1:
                    doublet = word[:-1] + c
                else:
                    doublet = word[:i] + c + word[i+1:]

                if (visited == None or doublet not in visited) and doublet in words:
                    doublets.add(doublet)

    return doublets


def check_base(words: list, start: str, end: str, **kwargs):
    """
    kwargs:
    - max_len: max length of route to be considered valid
    - func: function called after checking the base (args passed: words, start, end)
    - visited: list of visited words (so that we don't visit them again)
    - doublet_dict: dict of doublets from words list
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

            if (start, end) in solved_dict:
                return solved_dict[(start, end)]

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
    visited = kwargs['visited']

    if doublet_dict and start in doublet_dict:
        non_sorted_doublets = doublet_dict[start] if visited == None else [
            w for w in doublet_dict[start] if w not in visited]
    else:
        non_sorted_doublets = get_doublets(words, start, visited)
        if doublet_dict != None:
            doublet_dict[start] = non_sorted_doublets

    if len(non_sorted_doublets) == 0:
        return None

    doublets = sorted(non_sorted_doublets, key=str_diff_closure(end))

    res = min_len = None
    for min_path_word in doublets:
        actual_inc = str_inc(end, start, min_path_word)
        if actual_inc < 0:
            inc = actual_inc if actual_inc > 0 else 0

            next_res = doublet_route_dfs(
                words, min_path_word, end, max_len=min_len, visited=visited.union([start]) if visited else None)
            if next_res:
                next_route, next_inc = next_res
                route = [start] + next_route
                inc += next_inc
                res = (route, inc)
                if inc == 0:
                    solved_dict[(start, end)] = res
                    return res
                else:
                    min_len = len(route)
            else:
                solved_dict[(start, end)] = res
                return res
    else:
        return doublet_route_bfs(words, start, end, visited=visited.copy() if visited else None)


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
    next_words = []

    visited = kwargs['visited']

    res = min_len = None

    if doublet_dict and start in doublet_dict:
        next_words.append(doublet_dict[start])
    else:
        start_doublets = get_doublets(words, start, visited)
        next_words.append(start_doublets)
        if doublet_dict != None:
            doublet_dict[start] = start_doublets

    if visited:
        visited.add(start)
    else:
        visited = set([start])

    current_len = 0
    while len(visited) < len(words) and len(next_results) > 0 and (min_len == None or current_len < min_len - 1):
        results, current_words = next_results, next_words
        next_results, next_words = list(), list()

        for index, (route, inc) in enumerate(results):
            for word in current_words[index]:
                if word not in visited:
                    if word == end:
                        route.append(word)
                        res = (route, inc)
                        solved_dict[(start, end)] = res
                        return res
                    else:
                        actual_word_inc = str_inc(end, route[-1], word)
                        word_inc = actual_word_inc if actual_word_inc > 0 else 0
                        acc_inc = inc + word_inc

                        visited.add(word)

                        if actual_word_inc < 0:
                            current_res = doublet_route_dfs(
                                words, word, end, max_len=min_len, visited=set(route))
                            if current_res:
                                res_route, res_inc = current_res
                                res_inc += acc_inc
                                min_len = len(res_route)
                                res = (route + res_route, res_inc)
                        else:
                            word_route = route.copy()
                            word_route.append(word)

                            if doublet_dict and word in doublet_dict:
                                word_doublets = doublet_dict[word]
                            else:
                                word_doublets = get_doublets(
                                    words, word, visited)

                            if len(word_doublets) > 0:
                                next_results.append(
                                    (word_route, acc_inc))
                                next_words.append(word_doublets)

        current_len += 1
    else:
        solved_dict[(start, end)] = res
        return res


"""
Global variables:
- doublet_dict: dict of doublets from words list
- solved_dict: dict of already computed solutions
"""
doublet_dict = solved_dict = None


def main():
    try:
        word = input()
        words = list()
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
                global doublet_dict, solved_dict
                doublet_dict, solved_dict = dict(), dict()

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

################################################################
# DEBUG AND TEST METHODS
################################################################
import random


def test_all(print_res=False):
    words = list()
    pairs = set()
    max_len = int(input('number between 1 and 25143: '))
    while len(words) < max_len:
        word = ''
        for i in range(16):
            random_letter = chr(random.randint(ord('a'), ord('z')))
            word += random_letter
        words.append(word)
        for w in words:
            pairs.add((w, word))
            pairs.add((word, w))

    started = False
    for pair in pairs:
        if started:
            if print_res:
                print()  # Empty line between cases
        else:
            started = True
            global doublet_dict, solved_dict
            doublet_dict, solved_dict = dict(), dict()

        word_one, word_two = pair
        res = doublet_route_dfs(words, word_one, word_two)
        if res:
            route, inc = res
            if print_res:
                print(*route, sep='\n')
        else:
            if print_res:
                print('No solution')


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
            global doublet_dict, solved_dict
            doublet_dict, solved_dict = dict(), dict()

        word_one, word_two = pair
        res = doublet_route_dfs(words, word_one, word_two)
        if res:
            route, inc = res
            print(*route, sep='\n')
        else:
            print('No solution')


# test_all()
