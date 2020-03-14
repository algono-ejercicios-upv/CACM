#include <string>   // for string datatype
#include <iostream> // for cin / cout (standard input/output)
#include <cstring>  // for the memset function

using namespace std;

#define MAX_TURTLES 200

int numberOfTurtles;

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

        string original[MAX_TURTLES], required[MAX_TURTLES];

        string turtle;
        for (int j = 0; j < numberOfTurtles && getline(cin, turtle); j++)
        {
            original[j] = turtle;
        }
        for (int j = 0; j < numberOfTurtles && getline(cin, turtle); j++)
        {
            required[j] = turtle;
        }
    }
}