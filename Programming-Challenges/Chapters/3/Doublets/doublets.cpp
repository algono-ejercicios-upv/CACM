#include <string>
#include <vector>
#include <list>
#include <algorithm>
#include <map>
#include <iostream>
#include <cstring>

using namespace std;

#define MAX_WORDS 25143
#define MAX_WORD_LEN 16

#define NULL_RES \
    pair<list<int>, int> { list<int>{}, 0 }

vector<string> words;
pair<list<int>, int> res;
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
pair<list<int>, int> doublet_route(int startIndex, int endIndex, bool bfs, int max_len);

pair<list<int>, int> doublet_route_dfs(int startIndex, int endIndex)
{
    vector<int> doublets = get_doublets(startIndex);
    if (doublets.empty())
    {
        return NULL_RES;
    }

    string start = words[startIndex];
    sort(doublets.begin(), doublets.end(), [start](int i, int j) -> bool { return cmp_diff(start, words[i], words[j]); });

    int min_len = 0;
    string end = words[endIndex];

    for (int i = 0; i < doublets.size(); i++)
    {
        if (!visited[i])
        {
            int doubletIndex = doublets[i];
            int actual_inc = str_inc(end, start, words[doubletIndex]);
            if (actual_inc < 0)
            {
                int inc = actual_inc > 0 ? actual_inc : 0;

                pair<list<int>, int> next_res = doublet_route(doubletIndex, endIndex, false, min_len);
                if (!next_res.first.empty())
                {
                    // TODO: Keep best res
                    next_res.first.push_front(startIndex);
                    next_res.second += inc;
                    if (next_res.second == 0)
                    {
                        return next_res;
                    }
                    else
                    {
                        // We dont need to check if next_res.first len is lower than the previous one,
                        // as it is already checked so that in case it was, next_res.first would be empty
                        min_len = next_res.first.size();
                    }
                }
            }
        }
    }

    if (res.first.empty())
    {
        res = doublet_route(startIndex, endIndex, true, 0);
    }

    visited[startIndex] = true;
    return res;
}

pair<list<int>, int> doublet_route_bfs(int startIndex, int endIndex)
{
    vector<pair<list<int>, int>> next_results = {{{startIndex}, 0}};
    vector<vector<int>> next_words = {get_doublets(startIndex)};

    int min_len = 0;

    visited[startIndex] = true;

    int current_len = 0;
    vector<pair<list<int>, int>> results;
    vector<vector<int>> current_words;
    while (current_len < min_len - 1 && next_results.size() > 0)
    {
        results = next_results, current_words = next_words;
        next_results = {}, next_words = {};

        for (int index = 0; index < results.size(); index++)
        {
            pair<list<int>, int> current_res = results[index];
            for (int wordIndex : current_words[index])
            {
                if (visited[wordIndex])
                {
                    continue; // Jump to next word
                }

                list<int> route = current_res.first;

                if (wordIndex == endIndex)
                {
                    route.push_back(wordIndex);
                    res = current_res;
                    return res;
                }

                int actual_word_inc = str_inc(words[endIndex], words[route.back()], words[wordIndex]);
                int word_inc = actual_word_inc > 0 ? actual_word_inc : 0;
                int acc_inc = current_res.second + word_inc;

                visited[wordIndex] = true;

                if (actual_word_inc < 0)
                {
                    current_res = doublet_route(wordIndex, endIndex, false, min_len);
                    if (!current_res.first.empty())
                    {
                        current_res.second += acc_inc;
                        min_len = current_res.first.size();
                        current_res.first.insert(current_res.first.begin(), route.begin(), route.end());
                        res = current_res;
                    }
                }
                else
                {
                    list<int> word_route = list<int>(route);
                    word_route.push_back(wordIndex);

                    vector<int> word_doublets = doublets_calculated[wordIndex] ? doublets_dict[wordIndex] : get_doublets(wordIndex);

                    if (!word_doublets.empty())
                    {
                        next_results.push_back({word_route, acc_inc});
                        next_words.push_back(word_doublets);
                    }
                }
            }
        }
        current_len++;
    }

    return res;
}

pair<list<int>, int> doublet_route(int startIndex, int endIndex, bool bfs = false, int max_len = 0)
{
    if (startIndex == endIndex)
    {
        return {{startIndex}, 0};
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
                    return NULL_RES;
                }
                else if (diff == max_len - 2)
                {
                    return (are_doublets(start, end) ? pair<list<int>, int>{list<int>{startIndex, endIndex}, 0} : NULL_RES);
                }
            }
            return bfs ? doublet_route_bfs(startIndex, endIndex) : doublet_route_dfs(startIndex, endIndex);
        }
        else
        {
            return NULL_RES;
        }
    }
}

int main()
{
    string word;
    for (int i = 0; i < MAX_WORDS && (cin >> word); i++)
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
        int startIndex = find(words.begin(), words.end(), start) - words.begin();
        int endIndex = find(words.begin(), words.end(), end) - words.begin();

        // Reset the visited array
        memset(visited, false, words_size);
        pair<list<int>, int> res = doublet_route(startIndex, endIndex);
        if (res.first.empty())
        {
            cout << "No solution" << endl;
        }
        else
        {
            for (int wordIndex : res.first)
            {
                cout << words[wordIndex] << endl;
            }
            cout << endl;
        }
    }
}