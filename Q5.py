# Write a function that finds all the occurrences of a certain pattern, that starts with “un”
# has unlimited number of letters and ends with “an”
#
# The function takes 1 parameter: the text to look into and returns the number of matches.
#
# Use only the things we have learned in class. Give some explanations besides the code.

def find_pattern(text):
    """
    Finds all the occurences of a certain pattern, that starts with "un" has unlimited number of letters and ends with
    "an".
    :param text:
    :return:
    """

    words_pattern = []
    words = text.split()
    punctuation = "!'^~.;,"
    count = 0

    for word in words:
        for p in punctuation:
            word = word.replace(p, "")
        if word[0:2] == "un" and word[-2:] == "an":
            words_pattern.append(word)
            count += 1
    print(words_pattern)
    print(f"There are {count} words that follow the pattern!")
    return count


find_pattern("Undhhdan, unhdhsgan! I like words that start with un and end with an, like ungsfan.")