class Candidate:
    def __init__(self, candidate_id: int, name: str):
        self.candidate_id = candidate_id
        self.name = name.strip()
        self.eligible = True


class Ballot:
    def __init__(self, result_str: str):
        self.result = [int(num_str) for num_str in result_str.split()]

    def get_winner(self, valid_candidate_ids: tuple = None):
        """
        :return: int
        :returns The id of the winner candidate, if any
        """
        if valid_candidate_ids == None:
            return result[0]
        else:
            for next_winner in self.result:
                if next_winner in valid_candidate_ids:
                    return next_winner
            else:
                return None


class Election:
    MAX_BALLOTS = 1000

    # Init from user input
    def __init__(self):
        number_of_candidates = int(input())

        self.candidates = [Candidate(candidate_id, name=input())
                           for candidate_id in range(1, number_of_candidates+1)]

        self.ballots = []
        try:
            for ballot_num in range(self.MAX_BALLOTS):
                next_ballot_str = input()
                if next_ballot_str:
                    self.ballots.append(Ballot(next_ballot_str))
                else:
                    break
        except EOFError as err:
            # End of file, so no more ballots, its ok
            pass

    def __init__(self, election_str: str):
        election_lines = election_str.splitlines()
        number_of_candidates = int(election_lines[0])

        candidates_str_list = election_lines[1:number_of_candidates+1]
        ballots_str_list = election_lines[number_of_candidates+1:]

        self.candidates = [Candidate(candidate_id, candidate_name) for candidate_id,
                           candidate_name in enumerate(candidates_str_list, start=1)]
        self.ballots = [Ballot(result_str)
                        for result_str in ballots_str_list]

    def get_candidate(self, candidate_id):
        # We can assume that the id is always the candidate position in the list + 1
        return self.candidates[candidate_id-1]

    def get_winners(self, valid_candidate_ids: tuple = None):
        """
        :return: tuple(Candidate)
        :returns The winner of the election, if any
        """
        if valid_candidate_ids == None:
            valid_candidate_ids = self.get_valid_candidate_ids()

        if len(valid_candidate_ids) > 0:
            results = self.get_results(valid_candidate_ids)
            min_wins_for_winner = len(results)/2

            resultCount = dict([(candidate_id, results.count(candidate_id))
                                for candidate_id in valid_candidate_ids])

            for candidate_id in results:
                if resultCount[candidate_id] > min_wins_for_winner:
                    # There is a winner!
                    return tuple([self.get_candidate(candidate_id)])
            else:
                # No winners yet, look for losers and make them not eligible
                lowestNumberOfVotes = min(resultCount.values())
                remaining_candidate_ids = []
                for candidate_id in results:
                    if resultCount[candidate_id] > lowestNumberOfVotes:
                        remaining_candidate_ids.append(candidate_id)

                if len(remaining_candidate_ids) > 0:
                    # Try again with the remaining candidates
                    return self.get_winners(tuple(remaining_candidate_ids))
                else:
                    # No remaining candidates; there was a tie
                    # return all candidates left
                    return tuple(candidate for candidate in self.candidates if candidate.candidate_id in valid_candidate_ids)

        else:
            return None

    def get_results(self, valid_candidate_ids: tuple = None):
        return tuple(ballot.get_winner(valid_candidate_ids) for ballot in self.ballots)

    def get_valid_candidate_ids(self):
        return tuple(candidate.candidate_id for candidate in self.candidates if candidate.eligible)


def election_from_multiple_inputs():
    number_of_cases = int(input())
    input()

    elections = [Election()
                 for case in range(number_of_cases)]

    print_election_results(elections)


def election_from_single_input():
    return election_from_single_input(input())


def election_from_single_input(my_input: str):
    number_of_cases_str, _, elections_str = my_input.partition("\n\n")

    number_of_cases = int(number_of_cases_str)
    elections = [Election(election_str) for election_str in elections_str.split(
        "\n\n", number_of_cases)]

    print_election_results(elections)


def print_election_results(elections: list):
    print_blank_line = False
    for election in elections:
        if print_blank_line:
            print("\n")

        winners = election.get_winners()
        if winners != None:
            print(*[winner.name for winner in winners], sep='\n', end='')
            print_blank_line = True

election_from_multiple_inputs()