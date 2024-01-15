import zero_code

def test_basic_scenario():
    assert zero_code.zero_code([2, 5, 7, 8, 9]) == [0, 5, 7, 8, 0]

def test_empty_list():
    assert zero_code.zero_code([]) == []

def test_single_element_list():
    assert zero_code.zero_code([5]) == [0]

def test_two_element_list():
    assert zero_code.zero_code([3, 7]) == [0, 0]

def test_negative_numbers():
    assert zero_code.zero_code([-2, 5, -7, 8, -9]) == [0, 5, -7, 8, 0]

def test_all_zeros():
    assert zero_code.zero_code([0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]

def test_mixed_numbers():
    assert zero_code.zero_code([2, 0, 7, 0, 9]) == [0, 0, 7, 0, 0]
