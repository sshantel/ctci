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

    if len(string1) == len(string2):
        return one_edit_replace(string1, string2)
    elif len(string1) + 1 == len(string2):
        return one_edit_insert(string1, string2)
    elif len(string1) - 1 == len(string2):
        return one_edit_insert(string2, string1)
    return False


def one_edit_replace(string1, string2):
    edited = False
    for string1, string2 in zip(string1, string2):
        print(zip(string1, string2))
        if string1 != string2:
            if edited:
                return False
            edited = True
    return True


def one_edit_insert(string1, string2):
    edited = False
    i = 0
    j = 0

    while i < len(string1) and j < len(string2):
        if string1[i] != string2[j]:
            if edited:
                return False
            edited = True
            j += 1
        else:
            i += 1
            j += 1

    return True


print(one_away("pale", "ple"))

