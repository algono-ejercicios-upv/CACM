#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <iostream>
#include <cstring>

using namespace std;

#define MAX_WORDS 25143
#define MAX_WORD_LEN 16

vector<string> words, res;
bool visited[MAX_WORDS];

map<string, vector<string>> doublets_dict;

int words_size = MAX_WORDS;

int str_diff(string one, string two) {
    if (one.length == two.length) {
        int diff = 0;
        for (int i = 0; i < one.length; i++) {
            char l_one = one[i], l_two = two[i];
            if (l_one != l_two) { diff++; }
        }
        return diff;
    } else {
        return -1;
    }
}

int str_inc(string ref, string before, string after) {
    return str_diff(after, ref) - str_diff(before, ref);
}

bool cmp_diff(string ref, string one, string two) {
    return (str_diff(ref, one) < str_diff(ref, two));
}

bool are_doublets(string one, string two) {
    if (one.length == two.length) {
        int diff = 0;
        for (int i = 0; i < one.length; i++) {
            char l_one = one[i], l_two = two[i];
            if (l_one != l_two) { 
                if (++diff > 1) { return false; }
            }
        }
        return diff == 1;
    } else {
        return false;
    }
}

vector<string> get_doublets(string word) {
    // If the word is not in the map, it creates a default value for you
    vector<string> doublets = doublets_dict[word];
    if (doublets.empty()) {
        for (string dict_word : words) {
            if (are_doublets(word, dict_word)) {
                doublets.push_back(dict_word);
            }
        }
    }
    return doublets;
}

vector<string> doublet_route(int startIndex, int endIndex, bool bfs = false, int max_len = 0) {
    string start = words[startIndex], end = words[endIndex];
    if (start == end) { return {start}; }
    else {
        int diff = str_diff(start, end);
        if (diff >= 0) {
            if (max_len > 0) {
                if (diff >= max_len - 1) { return {}; }
                else if (diff == max_len - 2) {
                    return are_doublets(start, end) ? vector<string>{start, end} : vector<string>{};
                }
            }
            return bfs ? doublet_route_bfs(startIndex, endIndex) : doublet_route_dfs(startIndex, endIndex);
        } else {
            return {};
        }
    }
}


// TODO: BFS and DFS algorithms
vector<string> doublet_route_dfs(int startIndex, int endIndex) {
    res = vector<string>{};
    string start = words[startIndex];
    
    vector<string> doublets = get_doublets(start);
    if (doublets.empty()) {
        return res;
    }

    sort(doublets.begin(), doublets.end(), [start](string i, string j) -> bool { return cmp_diff(start, i, j); });

    int min_len = 0;
    string end = words[endIndex];

    for (int i = 0; i < doublets.size(); i++) {
        if (!visited[i]) {
            string doublet = doublets[i];
            int actual_inc = str_inc(end, start, doublet);
            if (actual_inc < 0) {
                int inc = actual_inc > 0 ? actual_inc : 0;

                vector<string> next_res = doublet_route(i, endIndex, false, min_len);
                if (!next_res.empty()) {
                    // TODO: Keep best res
                }
            }
        }
    }

    if (res.empty()) {
        res = doublet_route(startIndex, endIndex, true);
    }

    visited[startIndex] = true;
    return res;
}

vector<string> doublet_route_bfs(int startIndex, int endIndex) {
    res = vector<string>{};
    for (int i = 0; i < 10; i++) {
        res.push_back(to_string(i));
    }
    return res;
}

int main() {
    string word;
    for (int i = 0; i < MAX_WORDS && (cin >> word); i++) {
        if (word.empty()) { break; }
        words.push_back(word);
    }
    words_size = words.size();

    string start, end;
    while (cin >> start >> end) {
        int startIndex = find(words.begin(), words.end(), start) - words.begin();
        int endIndex = find(words.begin(), words.end(), end) - words.begin();

        // Reset the visited array
        memset(visited, false, words_size);
        vector<string> res = doublet_route(startIndex, endIndex);
        if (res.empty()) {
            cout << "No solution" << endl;
        } else {
            for (string word : res) {
                cout << word << endl;
            }
        }
    }
}