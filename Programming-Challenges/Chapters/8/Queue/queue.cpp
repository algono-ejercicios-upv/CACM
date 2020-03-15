#include <iostream>  // cin / cout
#include <algorithm> // next_permutation

using namespace std;

#define MAX_CASES 10000
#define MAX_PEOPLE 13

int n;

// Important: Each person has a different height
int people[MAX_PEOPLE];

// P valid if all members to the left are lower than this one
bool pValid(int pos)
{
    for (int i = pos - 1; i >= 0; i--)
    {
        if (people[i] >= people[pos])
        {
            return false;
        }
    }
    return true;
}

// R valid if all members to the right are lower than this one
bool rValid(int pos)
{
    for (int i = pos + 1; i < n; i++)
    {
        if (people[i] >= people[pos])
        {
            return false;
        }
    }
    return true;
}

bool valid(int p, int r)
{
    int cp = 0, cr = 0;
    for (int i = 0; i < n; i++)
    {
        if (pValid(i))
        {
            if (++cp > p) { return false; }
        }
        if (rValid(i))
        {
            if (++cr > r) { return false; }
        }
    }
    return p == cp && r == cr;
}

// 1 <= n <= 13
int permutations(const int p, const int r)
{
    if (p < 1 || r < 1)
    {
        return 0;
    }
    int result = 0;

    // Fill order must be ascending for all permutations to be checked (0-1-2) -> (2-1-0)
    for (int i = 0; i < n; i++)
    {
        people[i] = i;
    }

    do
    {
        if (valid(p, r))
        {
            result++;
        }
    } while (next_permutation(people, people + n));

    return result;
}

int debug()
{
    n = 3;
    cout << permutations(1, 2) << endl;
    return 0;
}

int main()
{
    // Code for optimization (Unties C and C++ standard streams, as it is not needed)
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    //return debug();

    // Get data from input

    int testCases;
    cin >> testCases;

    int p, r;
    for (int i = 0; i < testCases && cin >> n >> p >> r; i++)
    {
        cout << permutations(p, r) << '\n';
    }
}