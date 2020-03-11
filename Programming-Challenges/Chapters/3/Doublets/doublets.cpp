#include <string>
#include <vector>
#include <stack>
#include <deque>
#include <algorithm> // sort, mismatch
#include <map>
#include <iostream> // cin/cout
#include <utility> // pair

using namespace std;

#define MAX_WORDS 25143
#define MAX_WORD_LEN 16

#define NULL_RES \
    pair<deque<int>, int> { deque<int>(), 0 }

vector<string> words;
pair<deque<int>, int> res;
bool visited[MAX_WORDS];

map<int, vector<int>> doublets_dict;
bool doublets_calculated[MAX_WORDS];

int words_size = MAX_WORDS;

int str_diff(string one, string two)
{
    int one_len = one.length();
    if (one_len == two.length())
    {
        int diff = 0;
        for (int i = 0; i < one_len; i++)
        {
            if (one[i] != two[i])
            {
                diff++;
            }
        }
        return diff;
    }
    else
    {
        return -1;
    }
}

int str_inc(string ref, string before, string after)
{
    return str_diff(after, ref) - str_diff(before, ref);
}

bool cmp_diff(string ref, string one, string two)
{
    return (str_diff(ref, one) < str_diff(ref, two));
}

bool are_doublets(string one, string two)
{
    if (one.length() == two.length())
    {
        int diff = 0;
        for (int i = 0; i < one.length(); i++)
        {
            char l_one = one[i], l_two = two[i];
            if (l_one != l_two)
            {
                if (++diff > 1)
                {
                    return false;
                }
            }
        }
        return diff == 1;
    }
    else
    {
        return false;
    }
}

vector<int> get_doublets(int wordIndex)
{
    if (doublets_calculated[wordIndex])
    {
        return doublets_dict[wordIndex];
    }
    else
    {
        vector<int> doublets = {};
        for (int i = 0; i < words_size; i++)
        {
            if (are_doublets(words[wordIndex], words[i]))
            {
                doublets.push_back(i);
            }
        }

        doublets_dict[wordIndex] = doublets;
        doublets_calculated[wordIndex] = true;
        
        return doublets;
    }
}

// This is called forward declaration, and it is used so that doublet_route can call dfs and bfs, and they can call doublet_route as well
bool doublet_route(int startIndex, int endIndex, int max_len);

bool doublet_route_dfs(int startIndex, int endIndex, int diff)
{
    vector<int> doublets = get_doublets(startIndex);
    if (doublets.empty())
    {
        return false;
    }

    string start = words[startIndex];
    sort(doublets.begin(), doublets.end(), [start](int i, int j) -> bool { return cmp_diff(start, words[i], words[j]); });

    int min_len = 0;
    string end = words[endIndex];
    int initResSize = res.first.size(), initInc = res.second;
    stack<int> bestRes;
    int bestInc;
    bool anyFound;
    for (int i = 0; i < doublets.size(); i++)
    {
        int doubletIndex = doublets[i];
        if (!visited[doubletIndex])
        {
            int actual_inc = str_inc(end, start, words[doubletIndex]);

            res.first.push_back(startIndex);
            res.second += actual_inc;

            visited[startIndex] = true;

            bool found = doublet_route(doubletIndex, endIndex, min_len);

            // visited should only be considered for the current path (because other paths containing this index could be shorter)
            visited[startIndex] = false;

            int nextSize = res.first.size() - initResSize;
            if (found)
            {
                anyFound = true;

                if (res.second == -(diff))
                {
                    return true;
                }
                // We dont need to check if next_res.first len is lower than the previous one,
                // as it is already checked so that in case it was, next_res.first would be empty
                min_len = res.first.size();

                // Undoing next steps, and keeping them as the best ones yet (if they are)
                bestRes = stack<int>{};
                for (int j = 0; j < nextSize; j++)
                {
                    bestRes.push(res.first.back());

                    res.first.pop_back();
                }
                bestInc = res.second - initInc;
                res.second = initInc;
            }
            else
            {
                // Undoing next steps without keeping them (as they are not a solution)
                for (int j = 0; j < nextSize; j++)
                {
                    res.first.pop_back();
                }
            }
        }
    }

    if (anyFound)
    {
        while (!bestRes.empty())
        {
            res.first.push_back(bestRes.top());
            bestRes.pop();
        }
        res.second += bestInc;
    }

    return anyFound;
}

bool doublet_route(int startIndex, int endIndex, int max_len = 0)
{
    if (startIndex == endIndex)
    {
        res.first.push_back(startIndex);
        return true;
    }
    else
    {
        string start = words[startIndex], end = words[endIndex];
        int diff = str_diff(start, end);
        if (diff >= 0)
        {
            if (max_len > 0)
            {
                if (diff >= max_len - 1 || (diff == max_len - 2 && diff > 1))
                {
                    return false;
                }
            }

            if (diff == 1) // diff == 1 is equivalent to are_doublets(start, end)
            {
                res.first.push_back(startIndex);
                res.first.push_back(endIndex);
                return true;
            }

            return doublet_route_dfs(startIndex, endIndex, diff);
        }
        else
        {
            return false;
        }
    }
}

void print_res(bool found)
{
    if (found && !res.first.empty())
    {
        while (!res.first.empty())
        {
            cout << words[res.first.front()] << endl;
            res.first.pop_front();
        }
    }
    else
    {
        cout << "No solution" << endl;
    }
    cout << endl;
}

int main()
{
    // Code for optimization (Unties C and C++ standard streams, which allows you to still use cin/cout, but not scanf/printf)
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string word;
    for (int i = 0; i < MAX_WORDS && getline(cin, word); i++)
    {
        if (word.empty())
        {
            break;
        }
        words.push_back(word);
    }
    words_size = words.size();

    string start, end;
    while (cin >> start >> end)
    {
        res = NULL_RES;

        int startIndex = find(words.begin(), words.end(), start) - words.begin();
        int endIndex = find(words.begin(), words.end(), end) - words.begin();

        bool found = doublet_route(startIndex, endIndex);
        print_res(found);
    }
}