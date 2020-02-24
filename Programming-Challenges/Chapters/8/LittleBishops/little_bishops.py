res_dict = dict()  # Paste here dict with results for all combinations

while True:
    n_str, _, k_str = input().partition(' ')
    n, k = int(n_str), int(k_str)

    if n == 0 and k == 0:
        break
    
    print(res_dict.get((n, k), 'No solution'))
