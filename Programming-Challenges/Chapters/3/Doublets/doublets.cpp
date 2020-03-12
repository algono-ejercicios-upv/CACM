#include <string>
#include <vector>
#include <queue>
#include <algorithm>     // sort, mismatch
#include <unordered_map> // unordered_map = Hash table (access O(1)), map = binary tree (access O(log n))
#include <iostream>      // cin/cout

using namespace std;

#define MAX_WORDS 25143
#define MAX_WORD_LEN 16

char words[MAX_WORDS][MAX_WORD_LEN];

unordered_map<string, int> wordIndexMap[MAX_WORD_LEN];
int indexToLenMap[MAX_WORD_LEN];

vector<int> doublets_dict[MAX_WORDS];
bool doublets_calculated[MAX_WORDS];

int results_linked_list[MAX_WORDS];

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
        vector<int> doublets;
        int wordLength = indexToLenMap[wordIndex];
        for (auto &doubletPair : wordIndexMap[wordLength])
        {
            int doubletIndex = doubletPair.second;
            if (are_doublets(wordIndex, doubletIndex, wordLength))
            {
                doublets.push_back(doubletIndex);
            }
        }

        doublets_dict[wordIndex] = doublets;
        doublets_calculated[wordIndex] = true;

        return doublets;
    }
}

bool doublet_route(int startIndex, int endIndex)
{
    queue<int> check_queue;
    bool visited[MAX_WORDS] = {};

    check_queue.push(startIndex);
    visited[startIndex] = true;
    results_linked_list[startIndex] = -1;

    while (!check_queue.empty())
    {
        startIndex = check_queue.front();
        check_queue.pop();

        for (int doubletIndex : get_doublets(startIndex))
        {
            if (!visited[doubletIndex])
            {
                visited[doubletIndex] = true;
                results_linked_list[doubletIndex] = startIndex;
                check_queue.push(doubletIndex);
            }
        }
        if (visited[endIndex])
        {
            return true;
        }
    }
    return false;
}

void print_res(int startIndex, bool found)
{
    if (found)
    {
        while (startIndex >= 0)
        {
            cout << words[startIndex] << endl;
            startIndex = results_linked_list[startIndex];
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
        int startIndex = wordIndexMap[start.length()][start];
        int endIndex = wordIndexMap[end.length()][end];

        // Reverse the start and end, because the results will be displayed in reversed order
        bool found = doublet_route(endIndex, startIndex);
        print_res(startIndex, found);
    }
}