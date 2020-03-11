#include <string>
#include <vector>
#include <stack>
#include <algorithm>
#include <map>
#include <iostream>
#include <cstring>

using namespace std;

#define MAX_WORDS 25143
#define MAX_WORD_LEN 16

#define NULL_RES \
    pair<stack<int>, int> { stack<int>(), 0 }

vector<string> words;
pair<stack<int>, int> res;
bool visited[MAX_WORDS];

map<int, vector<int>> doublets_dict;
bool doublets_calculated[MAX_WORDS];

int words_size = MAX_WORDS;

int str_diff(string one, string two)
{
    if (one.length() == two.length())
    {
        int diff = 0;
        for (int i = 0; i < one.length(); i++)
        {
            char l_one = one[i], l_two = two[i];
            if (l_one != l_two)
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
        doublets_calculated[wordIndex] = true;
        return doublets;
    }
}

// This is called forward declaration, and it is used so that doublet_route can call dfs and bfs, and they can call doublet_route as well
bool doublet_route(int startIndex, int endIndex, int max_len);

bool doublet_route_dfs(int startIndex, int endIndex)
{
    vector<int> doublets = get_doublets(startIndex);
    if (doublets.empty())
    {
        visited[startIndex] = true;
        return false;
    }

    string start = words[startIndex];
    sort(doublets.begin(), doublets.end(), [start](int i, int j) -> bool { return cmp_diff(start, words[i], words[j]); });

    int min_len = 0;
    string end = words[endIndex];
    bool anyFound;
    pair<stack<int>, int> initRes = {stack<int>(res.first), res.second}, bestRes;
    for (int i = 0; i < doublets.size(); i++)
    {
        if (!visited[i])
        {
            int doubletIndex = doublets[i];

            int actual_inc = str_inc(end, start, words[doubletIndex]);
            int inc = actual_inc > 0 ? actual_inc : 0;

            res = {stack<int>(initRes.first), initRes.second + inc};
            res.first.push(startIndex);

            bool found = doublet_route(doubletIndex, endIndex, min_len);
            if (found)
            {
                anyFound = true;
                bestRes = res;
                if (res.second == 0)
                {
                    visited[startIndex] = true;
                    return true;
                }
                // We dont need to check if next_res.first len is lower than the previous one,
                // as it is already checked so that in case it was, next_res.first would be empty
                min_len = res.first.size();
            }
        }
    }

    visited[startIndex] = true;
    res = anyFound ? bestRes : initRes;
    return anyFound;
}

bool doublet_route(int startIndex, int endIndex, int max_len = 0)
{
    if (startIndex == endIndex)
    {
        res.first.push(startIndex);
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
                if (diff >= max_len - 1)
                {
                    return false;
                }
                else if (diff == max_len - 2)
                {
                    if (are_doublets(start, end))
                    {
                        res.first.push(startIndex);
                        res.first.push(endIndex);
                        return true;
                    }
                    else
                    {
                        return false;
                    }
                }
            }
            return doublet_route_dfs(startIndex, endIndex);
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
        int res_size = res.first.size();
        int i = res_size - 1;
        int resRoute[res_size];
        while (!res.first.empty())
        {
            resRoute[i] = res.first.top();
            res.first.pop();
            i--;
        }

        for (int wordIndex : resRoute)
        {
            cout << words[wordIndex] << endl;
        }
    }
    else
    {
        cout << "No solution" << endl;
    }
    cout << endl;
}

void debug()
{
    words = {
        "booster",
        "rooster",
        "roaster",
        "coasted",
        "roasted",
        "coastal",
        "postal"};

    // words = {
    //     "hola",
    //     "bola",
    //     "cola",
    //     "mola",
    //     "mala",
    //     "bala",
    //     "sala",
    //     "sota",
    //     "cota",
    //     "bota",
    //     "rota"};

    words_size = words.size();

    vector<pair<string, string>> pairs = {
        {"booster", "roasted"},
        {"coastal", "postal"}};

    // vector<pair<string, string>> pairs = {
    //     {"hola", "rota"},
    //     {"sala", "sota"}};

    res = NULL_RES;
    for (pair<string, string> word_pair : pairs)
    {
        string start = word_pair.first, end = word_pair.second;
        int startIndex = find(words.begin(), words.end(), start) - words.begin();
        int endIndex = find(words.begin(), words.end(), end) - words.begin();

        // Reset the visited array
        memset(visited, false, words_size);
        bool found = doublet_route(startIndex, endIndex);
        print_res(found);
    }
}

int main()
{
    // Code for optimization (Unties C and C++ standard streams, which allows you to still use cin/cout, but not scanf/printf)
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // CODE FOR DEBUGGING. TODO: DELETE FOR PRODUCTION
    // debug();
    // return 0;

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

    res = NULL_RES;
    string start, end;
    while (cin >> start >> end)
    {
        int startIndex = find(words.begin(), words.end(), start) - words.begin();
        int endIndex = find(words.begin(), words.end(), end) - words.begin();

        // Reset the visited array
        memset(visited, false, words_size);
        bool found = doublet_route(startIndex, endIndex);
        print_res(found);
    }
}