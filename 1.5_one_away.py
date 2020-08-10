"""
There are three types of edits that can be performed on strings:
insert a character, remove a character, or replace a character. Given 
two strings, write a function to check if they are one edit (or zero edits) away.
>>> pale, ple
True
>>> pales, pale
True
>>> pale, bale
True
>>> pale, bake
False
"""


def one_away(string1, string2):

    for char in string1:
        count = 0
        len_string_1 = len(string1)
        len_string_2 = len(string2)
        list_of_words = []
        if abs(len_string_1 - len_string_2) == 1:
            continue
        for i in range(len_string_1):
            if string1[i] != string2[i]:
                count += 1
            if count == 2:
                break
        if count == 1:
            list_of_words.append(char)
    return count == 1


print(one_away("pale", "ale"))

