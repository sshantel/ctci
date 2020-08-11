"""
Write a method to replace all spaces in a string with '%20'. You may assume
that the string has sufficient space at the end to hold the additional characters, 
and that you are given the "true" length of the string.
(Note: if implementing in Java, please use a character array so that you can perform 
this operation in place.)

>>> to_urlify('Mr John Smith    ', 13)
'Mr%20John%20Smith'

>>> to_urlify('cracking the coding interview', 29)
'cracking%20the%20coding%20interview'
"""


# def to_urlify(string):
#     return string.strip().replace(" ", "%20")

# n = size of string - ignoring ending white spaces


def to_urlify(string, n):
    string_list = list(string)
    for index, element in enumerate(string_list):
        if element == " ":
            string_list[index] = "%20"
    return "".join(string_list)


if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED. AWESOMESAUCE!\n")
