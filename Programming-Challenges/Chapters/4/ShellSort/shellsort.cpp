#include <string>
#include <vector>
#include <iostream>      // for cin / cout (standard input/output)
#include <unordered_map> // hash table (access O(1))
#include <algorithm>     // sort

using namespace std;

#define MAX_TURTLES 200

int numberOfTurtles;

string original[MAX_TURTLES];
unordered_map<string, int> required;

int dist[MAX_TURTLES];

vector<int> results;

vector<int> shellSort()
{
    results = {};
    for (int i = 0; i < numberOfTurtles; i++)
    {
        dist[i] = required[original[i]] - i;
        if (dist[i] < 0)
        {
            results.push_back(i);
            int reduction = 1;
            for (int j = i - 1; j >= 0; j--)
            {
                dist[j] -= reduction;
                if (dist[j] < 0)
                {
                    results.push_back(j);
                    reduction++;
                }
            }
        }
    }
    return results;
}

int greaterRequiredPos(int i, int j)
{
    return required[original[i]] > required[original[j]];
}

void printResults(vector<int> results)
{
    sort(results.begin(), results.end(), greaterRequiredPos);

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

    bool notFirst = false;
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

        if (notFirst)
        {
            cout << '\n';
        } // Print a new line between cases
        else
        {
            notFirst = true;
        }

        printResults(shellSort());
    }
}