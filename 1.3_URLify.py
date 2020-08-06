"""
Write a method to replace all spaces in a string with '%20'. You may assume
that the string has sufficient space at the end to hold the additional characters, 
and that you are given the "true" length of the string.
(Note: if implementing in Java, please use a character array so that you can perform 
this operation in place.)

>>> to_urlify('Mr John Smith    ', 13)
'Mr%20John%20Smith'

>>> to_urlify('cracking the coding interview')
'cracking%20the%20coding%20interview'
"""


def to_urlify(string):
    urlify_string = ""
    split_string = string.split()

    for char in split_string:
        urlify_string = char + "%20"

    return urlify_string
