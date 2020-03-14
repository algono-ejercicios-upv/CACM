#include <string>
#include <set>
#include <iostream>      // for cin / cout (standard input/output)
#include <unordered_map> // hash table (access O(1))
#include <algorithm>     // sort

using namespace std;

#define MAX_TURTLES 200

int numberOfTurtles;

string original[MAX_TURTLES];
unordered_map<string, int> required;

int dist[MAX_TURTLES];

struct resultComparator
{
    inline bool operator()(const int &left, const int &right)
    {
        return required[original[left]] > required[original[right]];
    }
};

set<int, resultComparator> results;

set<int, resultComparator> shellSort()
{
    results = set<int, resultComparator>{};
    for (int i = 0; i < numberOfTurtles; i++)
    {
        dist[i] = required[original[i]] - i;
        if (dist[i] < 0)
        {
            results.insert(i);
            int reduction = 1;
            for (int j = i - 1; j >= 0; j--)
            {
                if (dist[j] >= 0)
                {
                    dist[j] -= reduction;
                    if (dist[j] < 0)
                    {
                        results.insert(j);
                        reduction++;
                    }
                }
            }
        }
    }
    return results;
}

void printResults(set<int, resultComparator> results)
{
    for (int resultIndex : results)
    {
        cout << original[resultIndex] << '\n';
    }
}

int main()
{
    // Code for optimization (Unties C and C++ standard streams, as it is not needed)
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // Get data from input

    int testCases;
    cin >> testCases;

    for (int i = 0; i < testCases; i++)
    {
        cin >> numberOfTurtles;

        cin.ignore(); // Ignore the rest of the line after the number of turtles

        string turtle;
        for (int j = 0; j < numberOfTurtles && getline(cin, turtle); j++)
        {
            original[j] = turtle;
        }
        for (int j = 0; j < numberOfTurtles && getline(cin, turtle); j++)
        {
            required[turtle] = j;
        }

        printResults(shellSort());
        cout << '\n'; // Print a blank line after each test case
    }
}