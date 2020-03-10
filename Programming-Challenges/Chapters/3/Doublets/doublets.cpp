#include <string>
#include <vector>
#include <iostream>

using namespace std;

#define MAX_WORDS 25143
#define MAX_WORD_LEN 16

string words[MAX_WORDS];
vector<string> res;

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
    vector<string> doublets;
    for (string dict_word : words) {
        if (are_doublets(word, dict_word)) {
            doublets.push_back(dict_word);
        }
    }
    return doublets;
}

vector<string> doublet_route(string start, string end, bool bfs = false, int max_len = 0) {
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
            return bfs ? doublet_route_bfs(start, end, max_len) : doublet_route_dfs(start, end, max_len);
        } else {
            return {};
        }
    }
}


// TODO: BFS and DFS algorithms
vector<string> doublet_route_dfs(string start, string end, int max_len = 0) {
    for (int i = 0; i < 10; i++) {
        res.push_back(to_string(i));
    }
    return res;
}

vector<string> doublet_route_bfs(string start, string end, int max_len = 0) {
    for (int i = 0; i < 10; i++) {
        res.push_back(to_string(i));
    }
    return res;
}

int main() {
    string word;
    for (int i = 0; i < MAX_WORDS && (cin >> word); i++) {
        if (word.empty()) { break; }
        words[i] = word;
    }

    string start, end;
    while (cin >> start >> end) {
        vector<string> res = doublet_route(start, end);
        if (res.empty()) {
            cout << "No solution" << endl;
        } else {
            for (string word : res) {
                cout << word << endl;
            }
        }
    }
}