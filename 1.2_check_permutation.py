"""
Check Permutation
Given two strings, write a method to decide if one is a permutation of the other.
>>> check_permutation('dog','god')
True
>>> check_permutation('lamp','car')
False
>>> check_permutation('     car', 'rac')
False
"""

# get lengths of both strings
def check_permutation(string1, string2):

    len_string1 = len(string1)
    len_string2 = len(string2)

    # if length of both strings are not equal, not a permutation
    if len_string1 != len_string2:
        return False

    # sort strings
    # sorted() function returns a stored list of the specified iterable object
    a = sorted(string1)
    string1 = " ".join(a)
    b = sorted(string2)
    string2 = " ".join(b)

    # compare sorted strings
    for i in range(0, len_string1, 1):
        if (string1[i]) != (string2[i]):
            return False
    return True


if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED. AWESOMESAUCE!\n")
