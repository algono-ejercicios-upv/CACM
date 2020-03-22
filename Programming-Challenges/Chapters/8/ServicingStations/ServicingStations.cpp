#include <iostream>
#include <algorithm>
#include <cstring>
#include <map>
#include <vector>

using namespace std;

#define MIN_TOWNS 3
#define MAX_TOWNS 35

int numberOfRoutes[MAX_TOWNS + 1];
map<int, vector<int>> townsByNumberOfRoutes;
int numberOfTownsWithRoutes;

int routes[MAX_TOWNS + 1][MAX_TOWNS];
bool visited[MAX_TOWNS + 1];

int servicing_stations(int n, int m)
{
    if (m == 0)
    {
        return n; // If there are no routes, each town must have a station
    }
    else if (n < 3)
    {
        return 1; // 1 and 2 towns, with m > 0, is always 1
    }
    else
    {
        int res = n - numberOfTownsWithRoutes;
        // Reverse iterator
        for (auto it = townsByNumberOfRoutes.rbegin(); it != townsByNumberOfRoutes.rend(); it++)
        {
            for (int town : (it->second))
            {
                if (!visited[town])
                {
                    visited[town] = true;
                    for (int k = 0; k < (it->first); k++)
                    {
                        visited[routes[town][k]] = true;
                    }
                    res++;
                }
            }
        }
        return res;
    }
}

void add_route(int from, int to)
{
    if (!visited[from])
    {
        numberOfTownsWithRoutes++;
        visited[from] = true;
    }

    routes[from][numberOfRoutes[from]++] = to;
}

int main()
{
    // Code for optimization (Unties C and C++ standard streams, as it is not needed)
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // Get data from input
    bool started = false;
    int n, m;
    while (cin >> n >> m)
    {
        // marks end of input
        if (n == 0 && m == 0)
        {
            return 0;
        }

        if (started)
        {
            townsByNumberOfRoutes.clear();
        }
        else
        {
            started = true;
        }

        numberOfTownsWithRoutes = 0;
        int m1, m2;
        for (int i = 0; i < m && cin >> m1 >> m2; i++)
        {
            add_route(m1, m2);
            add_route(m2, m1);
        }

        memset(visited, false, MAX_TOWNS + 1);

        for (int i = 1; i <= n; i++)
        {
            townsByNumberOfRoutes[numberOfRoutes[i]].push_back(i);
        }

        cout << servicing_stations(n, m) << '\n';
    }
}