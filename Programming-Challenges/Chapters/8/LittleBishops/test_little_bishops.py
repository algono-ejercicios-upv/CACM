import little_bishops_lib

def test_little_bishops():
    assert little_bishops_lib.little_bishops(1, 0) == 1
    assert little_bishops_lib.little_bishops(1, 1) == 1
    assert little_bishops_lib.little_bishops(2, 1) == 4
    assert little_bishops_lib.little_bishops(2, 2) == 4
    assert little_bishops_lib.little_bishops(2, 3) == 0
    assert little_bishops_lib.little_bishops(3, 1) == 9
    assert little_bishops_lib.little_bishops(3, 2) == 26
    assert little_bishops_lib.little_bishops(3, 3) == 26
    assert little_bishops_lib.little_bishops(3, 4) == 8
    assert little_bishops_lib.little_bishops(4, 2) == 92
    assert little_bishops_lib.little_bishops(4, 3) == 232
    assert little_bishops_lib.little_bishops(4, 4) == 260
    assert little_bishops_lib.little_bishops(4, 5) == 112
    assert little_bishops_lib.little_bishops(5, 2) == 240
    assert little_bishops_lib.little_bishops(5, 3) == 1124
    assert little_bishops_lib.little_bishops(5, 4) == 2728
    assert little_bishops_lib.little_bishops(5, 5) == 3368
    assert little_bishops_lib.little_bishops(6, 2) == 520
    assert little_bishops_lib.little_bishops(6, 3) == 3896
    assert little_bishops_lib.little_bishops(6, 4) == 16428
    assert little_bishops_lib.little_bishops(8, 6) == 5599888

def test_little_bishops_exhaustive():
    res_dict = dict()
    for n in range(1,9):
        for k in range(0,(n**2)+1):
            res_dict[(n,k)] = little_bishops_lib.little_bishops(n, k)
    
    raise Exception("res_str = " + little_bishops_lib.dict_str(res_dict))