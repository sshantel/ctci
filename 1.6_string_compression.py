"""
Implement a method to perform basic string compression using the counts of repeated characters.
For example, the string aabcccccaaa would become a2b1c5a3.
If the 'compressed' string would not become smaller than the original string,
your method should return the original string. You can assume the string has only uppercase and lowercase
ase letters(a-z).
>>> string_compression('aabcccccaaa')
'a2b1c5a3'
"""


def string_compression(string):

    compressed = []
    current = ""
    count = 0

    for char in string:
        if char != current:
            compressed.append(current)

            if count >= 1:
                compressed.append(str(int(count)))

            current = char
            count = 0

        count += 1

    compressed.append(current)
    if count > 1:
        compressed.append(str(int(count)))

    return "".join(compressed)


if __name__ == "__main__":
    import doctest
result = doctest.testmod()
if doctest.testmod().failed == 0:
    print("\n✨ ALL TESTS PASSED!\n")
