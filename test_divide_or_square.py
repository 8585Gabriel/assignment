import divide_or_square

def test_divisible_by_5():
    assert divide_or_square.divide_or_square(25) == 5.0

def test_not_divisible_by_5():
    assert divide_or_square.divide_or_square(7) == 2

def test_negative_number_divisible_by_5():
    assert divide_or_square.divide_or_square(-25) == 5.0

def test_negative_number_not_divisible_by_5():
    assert divide_or_square.divide_or_square(-7) == 3

def test_zero():
    assert divide_or_square.divide_or_square(0) == 0

def test_large_number_divisible_by_5():
    assert divide_or_square.divide_or_square(10000) == 100.0

def test_large_number_not_divisible_by_5():
    assert divide_or_square.divide_or_square(10001) == 1
