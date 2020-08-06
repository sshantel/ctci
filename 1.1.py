"""
Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
>>> is_unique('abcdefghijklmnopqrstuvwxyz')
True
>>> is_unique('computer')
True
>>> is_unique('book')
False
>>> is_unique('lamp')
True
"""


def is_unique(string):
    if len(string) > 256:
        return False

    else:
        char_set = {}
        for char in string:
            if char not in char_set:
                char_set[char] = 1
            else:
                return False

        return True


if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED.\n")
