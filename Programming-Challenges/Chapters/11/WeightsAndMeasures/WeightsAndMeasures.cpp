#include <iostream> // cin / cout
#include <vector>
#include <algorithm> // sort
#include <climits>   // INT_MAX

using namespace std;

class Turtle
{
public:
    int weight, strength;

    Turtle(int w, int c) : weight{w}, strength{c}
    {
    }

    bool operator<(const Turtle &other) const
    {
        return this->strength < other.strength || (this->strength == other.strength && this->weight > other.weight);
    }
};

vector<Turtle> turtles;

int getMaxStackLength()
{
    int n = turtles.size() + 1;
    int *accumulated_weight = new int[n];

    // We start on the element #1 because of what we do just below
    fill(accumulated_weight + 1, accumulated_weight + n, INT_MAX);

    // The accumulated weight of the empty stack is zero
    accumulated_weight[0] = 0;

    // Before starting, the unique stack is the empty stack.
    int max_length = 0;

    // For all turtles sorted appropriately:
    for (unsigned int i = 0; i < turtles.size(); ++i)
    {
        // For all stack till now.
        for (int j = max_length; j >= 0; --j)
        {
            // Try to extend every existing stack with the i-th turtle.
            int w = accumulated_weight[j] + turtles[i].weight;

            // If it could be, then extend it.
            if (w <= turtles[i].strength && w < accumulated_weight[j + 1])
            {
                accumulated_weight[j+1] = w; // for stacks of the same length (j+1), choose the one with the minimum weight
                max_length = max(max_length, j+1); // update the length of the highest stack till turtle 'i'
            }
        }
    }

    return max_length;
}

int main()
{
    // Code for optimization (Unties C and C++ standard streams, as it is not needed)
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int w, s;
    while (cin >> w >> s)
    {
        turtles.push_back(Turtle(w, s));
    }

    sort(turtles.begin(), turtles.end());

    int max = getMaxStackLength();
    cout << max << '\n';
}
