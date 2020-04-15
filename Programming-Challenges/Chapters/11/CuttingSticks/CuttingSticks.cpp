#include <iostream> // cin / cout
#include <climits>  // INT_MAX

using namespace std;

const static int INFINIT = INT_MAX / 2;

static int positions[1001];

struct cut
{
    int left, right, cost;
};

static struct cut dp[50+3][50+3];

int get_minimum_cutting(int l, int n)
{
    // Reset dp
    for (int i = 0; i <= n; i++)
    {
        for (int j = 0; j <= n; j++)
        {
            dp[i][j].cost = INFINIT;
            dp[i][j].left = -1;
            dp[i][j].right = -1;
        }
    }

    // Trivial cases
    for (int i = 0; i < n - 1; i++)
    {
        int row = n - 2 - i;
        int col = i;
        dp[row][col].left = positions[i];
        dp[row][col].right = positions[i + 1];
        dp[row][col].cost = 0;
    }

    for (int i = n - 3; i >= 0; i--)
    {
        for (int j = n - 3 - i; j >= 0; j--)
        {
            int k = n - 2 - j;
            int l = j + 1;

            while (k > i)
            {
                int new_cost = dp[i][l].cost + dp[k][j].cost + dp[i][l].right - dp[k][j].left;

                if (new_cost < dp[i][j].cost)
                {
                    dp[i][j].cost = new_cost;
                    dp[i][j].left = dp[k][j].left;
                    dp[i][j].right = dp[i][l].right;
                }

                k--;
                l++;
            }
        }
    }

    return dp[0][0].cost;
}

int main()
{
    // Code for optimization (Unties C and C++ standard streams, as it is not needed)
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int l, n;

    while (cin >> l && l > 0)
    {
        cin >> n;
        
        positions[0] = 0;
        for (int i = 1; i <= n; i++)
        {
            cin >> positions[i];
        }
        positions[n + 1] = l;

        cout << "The minimum cutting is " << get_minimum_cutting(l, n + 2) << ".\n";
    }
}