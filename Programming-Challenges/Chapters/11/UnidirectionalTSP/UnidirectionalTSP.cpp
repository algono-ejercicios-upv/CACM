#include <iostream> // cin / cout
#include <climits>  // INT_MAX

using namespace std;

const static int M = 10, N = 100;

static int cells[M][N];

struct State
{
    int accumulated_cost;
    int next;
};

static struct State dp[M][N];

int main()
{
    // Code for optimization (Unties C and C++ standard streams, as it is not needed)
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int m, n;
    bool rc = true;
    while (cin >> m >> n)
    {
        int w;
        for (int r = 0; r < m && rc; r++)
        {
            for (int c = 0; c < n && rc; c++)
            {
                rc = (bool)(cin >> w);
                if (rc)
                    cells[r][c] = w;
            }
        }
        for (int r = 0; r < m; r++)
        {
            dp[r][n - 1].accumulated_cost = cells[r][n - 1];
            dp[r][n - 1].next = r;
        }

        for (int c = n - 1; c > 0; c--)
        {
            for (int r = 0; r < m; r++)
            {
                dp[r][c - 1].accumulated_cost = INT_MAX;
            }

            for (int r = 0; r < m; r++)
            {
                int previous_row = (r - 1 + m) % m;
                int current_row = r;
                int next_row = (r + 1) % m;

                int p_cost = dp[r][c].accumulated_cost + cells[previous_row][c - 1];
                int c_cost = dp[r][c].accumulated_cost + cells[current_row][c - 1];
                int n_cost = dp[r][c].accumulated_cost + cells[next_row][c - 1];

                if (c_cost < dp[current_row][c - 1].accumulated_cost)
                {
                    dp[current_row][c - 1].accumulated_cost = c_cost;
                    dp[current_row][c - 1].next = r;
                }
                if (p_cost < dp[previous_row][c - 1].accumulated_cost)
                {
                    dp[previous_row][c - 1].accumulated_cost = p_cost;
                    dp[previous_row][c - 1].next = r;
                }
                if (n_cost < dp[next_row][c - 1].accumulated_cost)
                {
                    dp[next_row][c - 1].accumulated_cost = n_cost;
                    dp[next_row][c - 1].next = r;
                }
            }
        }

        // Searches the best row in the first column
        int best_row = 0;
        for (int r = 1; r < m; r++)
        {
            if (dp[r][0].accumulated_cost < dp[best_row][0].accumulated_cost)
            {
                best_row = r;
            }
        }

        // Reconstructs the path by printing the number of each row directly
        int row = best_row;
        cout << row + 1;
        for (int c = 1; c < n; c++)
        {
            row = dp[row][c - 1].next;
            cout << ' ' << row + 1;
        }
        cout << '\n'
             << dp[best_row][0].accumulated_cost << '\n';
    }
    return 0;
}