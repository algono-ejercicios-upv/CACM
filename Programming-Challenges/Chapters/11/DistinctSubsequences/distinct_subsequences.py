def number_of_subsequences(word: str, subsequence: str):
    dp = [[] for _ in range(len(subsequence))]
    for i in range(len(subsequence)):
        acc = 0
        for j in range(i, len(word)):
            v = 0
            if subsequence[i] == word[j]:
                if i > 0:
                    # No need to check if j > 0, cause we know that j >= i is always True
                    v = dp[i-1][j-i]
                else:
                    v = 1
            acc += v
            dp[i].append(acc)
    #print(dp)
    return acc

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
