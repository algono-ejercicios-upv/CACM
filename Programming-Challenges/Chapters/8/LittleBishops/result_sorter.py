import little_bishops_lib
import result

disordered = result.res_dict
sorted_dict = {k: disordered[k] for k in sorted(disordered)}
print('res_dict = ' + little_bishops_lib.dict_str(sorted_dict))