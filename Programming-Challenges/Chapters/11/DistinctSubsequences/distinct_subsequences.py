def number_of_subsequences(word: str, subsequence: str):
    dp = [[0] * len(word) for _ in range(len(subsequence))]
    for i, sub_letter_matches in enumerate(dp):
        for j, word_letter_matches in enumerate(sub_letter_matches):
            if subsequence[i] == word[j]:
                if i > 0:
                    ci, cj = i-1, j-1
                    while cj >= 0:
                        word_letter_matches += dp[ci][cj]
                        cj -= 1
                else:
                    word_letter_matches = 1
                dp[i][j] = word_letter_matches
    print(dp)
    return sum(dp[-1])

def main():
    try:
        cases = int(input())
        for case in range(cases):
            word = input()
            subsequence = input()
            print(number_of_subsequences(word, subsequence))
    except EOFError as err:
        pass


main()
