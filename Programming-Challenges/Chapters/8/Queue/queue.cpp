#include <iostream>  // cin / cout

using namespace std;

#define MAX_CASES 10000
#define MAX_PEOPLE 13

// precomputedResults[n][p][r]
int precomputedResults[MAX_PEOPLE+1][MAX_PEOPLE+1][MAX_PEOPLE+1];
bool resultsAvailable[MAX_PEOPLE+1][MAX_PEOPLE+1][MAX_PEOPLE+1];

int permutations_base(int n, int p, int r)
{
    if (p < 1 || r < 1 || p > n || r > n)
    {
        return 0;
    }
    else if (p == n)
    {
        return (r == 1) ? 1 : 0;
    }
    else if (r == n)
    {
        return (p == 1) ? 1 : 0;
    }
    else if (n == 1)
    {
        return (p == 1 && r == 1) ? 1 : 0;
    }
    else if (n == 2)
    {
        return p ^ r; // p xor r
    }
    else
    {
        return -1; // No base solution
    }
}

// 1 <= n <= 13
int permutations(int n, int p, int r)
{
    int res = permutations_base(n, p, r);
    if (res < 0) // Wasn't a base case, do recursive calculation
    {
        if (resultsAvailable[n][p][r])
        {
            return precomputedResults[n][p][r];
        }
        else
        {
            // Position of person with min height: 1 time first, (n-2) times middle, and 1 time last
            // Thus, 1 * first + (n-2) * middle + 1 * last
            res = permutations(n - 1, p - 1, r) + (n - 2) * permutations(n - 1, p, r) + permutations(n - 1, p, r - 1);

            // Add res to precomputed results
            precomputedResults[n][p][r] = res;
            resultsAvailable[n][p][r] = true;
        }
    }
    return res;
}

int main()
{
    // Code for optimization (Unties C and C++ standard streams, as it is not needed)
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // Get data from input

    int testCases;
    cin >> testCases;

    int n, p, r;
    for (int i = 0; i < testCases && cin >> n >> p >> r; i++)
    {
        cout << permutations(n, p, r) << '\n';
    }
}