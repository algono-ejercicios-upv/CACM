from little_bishops_lib import dict_str

n_start_str, _, k_start_str = input().partition(' ')
n_start, k_start = int(n_start_str), int(k_start_str)

input()

res_dict = dict()

for k in range(k_start, (n_start**2)+1):
    res_dict[(n_start, k)] = int(input())

for n in range(n_start+1, 9):
    for k in range(0, (n**2)+1):
        res_dict[(n, k)] = int(input())

print(dict_str(res_dict))