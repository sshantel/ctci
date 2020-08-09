"""
Given a string, write a function to check if it is a permutation of a palindrome.  
A palindrome is a word or phrase that is the same forwards and backwards.
A permutation is a rearrangement of letters. The palindrome does not need to be limited
to just dictionary words.
>>> palindrome_permutation('Tact Coa')
True
"""


def palindrome_permutation(string):
    lowercase_string = string.lower()
    length = len(lowercase_string)
    string_list = []
    # print(lowercase_string)

    def create_pairs_list(poop):
        for character in poop:
            try:
                string_list.remove(character)
            except ValueError:
                string_list.append(character)
        return string_list

    the_list = create_pairs_list(lowercase_string)
    # print(the_list)

    if length % 2 == 0:
        # print("hi")
        return the_list == []
    else:
        return len(the_list) == 1


print(palindrome_permutation("pooopa"))

if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED. AWESOMESAUCE!\n")
