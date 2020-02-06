ERDOS = "Erdos, P."
INFINITY = "infinity"


def calculate_erdos_numbers():
    # Get input from scenario
    try:
        number_of_papers_str, _, number_of_names_str = input().partition(' ')
        number_of_papers = int(number_of_papers_str)
        number_of_names = int(number_of_names_str)

        papers = [input() for paper in range(number_of_papers)]
        names = [input() for name in range(number_of_names)]
    except EOFError as err:
        pass

    names_and_last_names_in_papers = [paper.split(":")[0] for paper in papers]
    names_in_papers = [set(map(lambda name, last_name: f"{name}, {last_name}", names_and_last_names_in_paper.split(
        ", ")[::2], names_and_last_names_in_paper.split(", ")[1::2])) for names_and_last_names_in_paper in names_and_last_names_in_papers]

    coauthors = dict()
    for paper_names in names_in_papers:
        for name in paper_names:
            name_coauthors = set(paper_names)
            name_coauthors.discard(name)
            if name in coauthors:
                coauthors.get(name).update(name_coauthors)
            else:
                coauthors.setdefault(name, name_coauthors)

    erdos_numbers = dict()
    current_authors = list()
    next_authors = list()

    for author in coauthors.get(ERDOS):
        erdos_numbers.setdefault(author, 1)
        next_authors.append(author)

    current_level = 1
    while len(next_authors) > 0:
        current_authors = next_authors
        next_authors = list()
        for author in current_authors:
            author_coauthors = coauthors.get(author, [])
            if len(author_coauthors) > 0:
                for coauthor in [author_coauthor for author_coauthor in author_coauthors if author_coauthor not in erdos_numbers]:
                    erdos_numbers.setdefault(coauthor, current_level + 1)
                    next_authors.append(coauthor)
        
        current_level += 1

    erdos_numbers_to_print = [
        f"{name} {erdos_numbers.get(name, INFINITY)}" for name in names]
    print(*erdos_numbers_to_print, sep="\n", end="")


try:
    number_of_cases = int(input())

    for scenario in range(1, number_of_cases+1):
        print(f"Scenario {scenario}")

        calculate_erdos_numbers()

        # Print a blank line in every scenario but the last one
        if (scenario < number_of_cases):
            print()
except EOFError as err:
    pass
