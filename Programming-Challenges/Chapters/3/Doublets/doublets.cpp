#include <string>
#include <vector>
#include <stack>
#include <deque>
#include <algorithm>     // sort, mismatch
#include <unordered_map> // unordered_map = Hash table (access O(1)), map = binary tree (access O(log n))
#include <iostream>      // cin/cout
#include <utility>       // pair

using namespace std;

#define MAX_WORDS 25143
#define MAX_WORD_LEN 16

#define NULL_RES \
    pair<deque<int>, int> { deque<int>(), 0 }

char words[MAX_WORDS][MAX_WORD_LEN];

unordered_map<string, int> wordIndexMap[MAX_WORD_LEN];
int indexToLenMap[MAX_WORD_LEN];

vector<int> doublets_dict[MAX_WORDS];
bool doublets_calculated[MAX_WORDS];

pair<deque<int>, int> res;

int words_size;

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

bool are_doublets(int one, int two, int len)
{
    int diff = 0;
    for (int i = 0; i < len; i++)
    {
        char l_one = words[one][i], l_two = words[two][i];
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

vector<int> get_doublets(int wordIndex)
{
    if (doublets_calculated[wordIndex])
    {
        return doublets_dict[wordIndex];
    }
    else
    {
        vector<int> doublets = doublets_dict[wordIndex];
        int wordLength = indexToLenMap[wordIndex];
        for (auto &doubletPair : wordIndexMap[wordLength])
        {
            int doubletIndex = doubletPair.second;
            if (are_doublets(wordIndex, doubletIndex, wordLength))
            {
                doublets.push_back(doubletIndex);
            }
        }

        doublets_calculated[wordIndex] = true;

        return doublets;
    }
}

// This is called forward declaration, and it is used so that doublet_route can call bfs, and bfs can call doublet_route as well
bool doublet_route(int startIndex, int endIndex, int max_len);

bool doublet_route_bfs(int startIndex, int endIndex, int diff)
{
    // TODO: Implement BFS
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

            return doublet_route_bfs(startIndex, endIndex, diff);
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
    words_size = 0;
    for (int i = 0; i < MAX_WORDS && getline(cin, word); i++)
    {
        if (word.empty())
        {
            break;
        }

        int word_length = word.length();

        for (int j = 0; j < word_length; j++)
        {
            words[i][j] = word[j];
        }
        wordIndexMap[word_length][word] = i;
        indexToLenMap[i] = word_length;
        words_size++;
    }

    string start, end;
    while (cin >> start >> end)
    {
        res = NULL_RES;

        int startIndex = wordIndexMap[start.length()][start];
        int endIndex = wordIndexMap[end.length()][end];

        bool found = doublet_route(startIndex, endIndex);
        print_res(found);
    }
}