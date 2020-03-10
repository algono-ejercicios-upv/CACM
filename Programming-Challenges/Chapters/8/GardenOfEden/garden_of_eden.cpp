#include <string> // for string datatype
#include <iostream> // for cin / cout (standard input/output)
#include <cstring> // for the memset function

using namespace std;

#define MAX_LEN 32
#define N_STATES 8

string a_state;
int a_id, a_len, first_state;
bool reachable, visited[MAX_LEN][N_STATES];

bool is_reachable(int cell_pos, int curr_state) {
    if (cell_pos == a_len-1) {
        return ((curr_state>>1)&1) == ((first_state>>2)&1) && (curr_state&1) == ((first_state>>1)&1);
    } else {
        visited[cell_pos][curr_state] = true;
        for (int i = 0; i < N_STATES; i++) {
            // (char - '0') is a way to convert char into an int faster
            // matches = rule number 'i' outputs the same number as the next cell's end state
            // and the last two digits of my current state match the first two of rule number 'i' 
            bool matches = ((a_id>>i)&1) == a_state[cell_pos+1]-'0' && ((curr_state>>1)&1) == ((i>>2)&1) && (curr_state&1) == ((i>>1)&1);
            if (matches) {
                // If that case was visited already, then it wasnt reachable
                // (In case it were, then it would have returned 'true' right away)
                if (!visited[cell_pos+1][i] && is_reachable(cell_pos+1, i)) {
                    return true;
                }
            }
        }
        return false;
    }
}

int main() {
    // Code for optimization (Unties C and C++ standard streams, which allows you to still use cin/cout, but not scanf/printf)
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    while (cin >> a_id >> a_len >> a_state) {
        reachable = false;
        for (int i = 0; i < N_STATES && !reachable; i++) {
            // If rule number 'i' outputs the same number as the first cell's end state
            if (((a_id>>i)&1) == a_state[0]-'0') {
                // Reset the visited array
                for (int j = 0; j < a_len; j++) {
                    memset(visited[j], false, N_STATES);
                }
                first_state = i;
                reachable = is_reachable(0, i);
            }
        }
        cout << (reachable ? "REACHABLE" : "GARDEN OF EDEN") << endl;
    }
}
