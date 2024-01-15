import check_duplicates

def test_duplicates_exist():
    assert check_duplicates.check_duplicates(['apple', 'orange', 'banana', 'apple']) == ['apple']

def test_no_duplicates():
    assert check_duplicates.check_duplicates(['Yoda', 'Moses', 'Joshua', 'Mark']) == "No duplicates"

def test_empty_list():
    assert check_duplicates.check_duplicates([]) == "No duplicates"

def test_single_duplicate():
    assert check_duplicates.check_duplicates(['apple', 'apple']) == ['apple']

def test_multiple_duplicates():
    assert check_duplicates.check_duplicates(['apple', 'orange', 'banana', 'apple', 'banana']) == ['apple', 'banana']

def test_case_sensitive_duplicates():
    assert check_duplicates.check_duplicates(['Apple', 'apple']) == "No duplicates"

def test_numbers_duplicates():
    assert check_duplicates.check_duplicates([1, 2, 3, 4, 4, 5, 6, 6]) == [4, 6]
