#include <iostream> // cin / cout
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <stack>

using namespace std;

class Elephant
{
public:
    int id;
    int w;
    int s;
    Elephant(int id, int w, int s) : id{id}, w{w}, s{s}
    {
    }
    bool operator<(Elephant &other)
    {
        return w < other.w;
    }

    bool canPrecede(Elephant &other)
    {
        return w < other.w && s > other.s;
    }
};

vector<Elephant> elephants;
unordered_map<int, int> pre, lengths;

int getLongestSequence()
{
    int longestLength = 0, lastMember = -1;

    for (int i = 0; i < elephants.size(); i++)
    {
        Elephant current = elephants[i];
        for (int j = i-1; j > 0; j--)
        {
            Elephant possiblePredecessor = elephants[j];
            if (possiblePredecessor.canPrecede(current))
            {
                int possibleLength = lengths[possiblePredecessor.id] + 1;
                if (possibleLength > lengths[current.id])
                {
                    lengths[current.id] = possibleLength;
                    pre[current.id] = possiblePredecessor.id;

                    if (possibleLength > longestLength)
                    {
                        longestLength = lengths[current.id];
                        lastMember = current.id;
                    }
                }
            }
        }
    }

    return lastMember;
}

int main()
{
    int w, s;
    for (int id = 1; cin >> w >> s; id++)
    {
        elephants.push_back(Elephant(id, w, s));
    }

    sort(elephants.begin(), elephants.end());

    int lastMember = getLongestSequence();
    cout << (lengths[lastMember] + 1) << '\n'; // lengths map is not counting itself

    stack<int> sequence;
    int currentId = lastMember;
    while (currentId > 0)
    {
        sequence.push(currentId);
        currentId = pre[currentId];
    }
    while (!sequence.empty())
    {
        cout << sequence.top() << '\n';
        sequence.pop();
    }
}