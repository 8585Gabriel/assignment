import only_floats

def test_both_floats():
    assert only_floats.only_floats(12.1, 23.0) == 2

def test_one_float():
    assert only_floats.only_floats(12.1, 23) == 1

def test_both_integers():
    assert only_floats.only_floats(12, 23) == 0

def test_negative_float():
    assert only_floats.only_floats(-12.1, 23.0) == 2

def test_zero_float():
    assert only_floats.only_floats(0.0, 0.0) == 2

def test_negative_integer_and_float():
    assert only_floats.only_floats(-12, 23.0) == 1

def test_string_and_float():
    assert only_floats.only_floats('hello', 23.0) == 1
