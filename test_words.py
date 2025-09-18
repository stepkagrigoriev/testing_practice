from main import bruteforce, dict_find

def test_bruteforce_empty():
    words = []
    assert bruteforce(words) == (0, None)

def test_bruteforce_single_word():
    words = ['hello']
    assert bruteforce(words) == (0, None)

def test_bruteforce_no_matches():
    words = ['abc', 'def', 'ghi']
    assert bruteforce(words) == (0, None)

def test_bruteforce_with_matches():
    words = ['abc', 'cde', 'def']
    assert bruteforce(words) == (2, ('cde', 'def'))

def test_bruteforce_multiple_matches():
    words = ['abcd', 'cdef', 'efgh', 'xyz']
    assert bruteforce(words) == (2, ('abcd', 'cdef')) or (2, ('cdef', 'efgh'))

def test_bruteforce_one_char_match():
    words = ['ab', 'a', 'bc']
    assert bruteforce(words) == (1, ('ab', 'a')) or (1, ('ab', 'bc'))

def test_bruteforce_same_words():
    words = ['abc', 'abc']
    assert bruteforce(words) == (0, None)

def test_dict_find_empty():
    words = []
    assert dict_find(words) == (0, None)

def test_dict_find_single_word():
    words = ['hello']
    assert dict_find(words) == (0, None)

def test_dict_find_no_matches():
    words = ['abc', 'def', 'ghi']
    assert dict_find(words) == (0, None)

def test_dict_find_with_matches():
    words = ['abc', 'cde', 'def']
    assert dict_find(words) == (2, ('cde', 'def'))

def test_dict_find_multiple_matches():
    words = ['abcd', 'cdef', 'efgh', 'xyz']
    assert bruteforce(words) == (2, ('abcd', 'cdef')) or (2, ('cdef', 'efgh'))

def test_dict_find_one_char_match():
    words = ['ab', 'a', 'bc']
    assert dict_find(words) == (1, ('ab', 'a')) or (1, ('ab', 'bc'))

def test_dict_find_same_words():
    words = ['abc', 'abc']
    assert dict_find(words) == (0, None)
