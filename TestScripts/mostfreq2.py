
def most_frequent(s):
    """Return the most frequently occuring word in s."""

    """ Step 1 - The following assumptions have been made:
        - Space is the default delimiter
        - There are no other punctuation marks that need removing
        - Convert all letters into lower case"""


    word_list_array = s.split()


    """Step 2 - sort the list alphabetically"""

    word_sort = sorted(word_list_array, key=str.lower)

    """Step 3 - count the number of times word has been repeated in the word_sort array.
                create another array containing the word and the frequency in which it is repeated"""

    wordfreq = []
    # freq_wordsort = []
    for w in word_sort:
        wordfreq.append(word_sort.count(w))
        # freq_wordsort = zip(wordfreq, word_sort)


    """Step 4 - output the array having the maximum first index variable and output the word in that array"""

    max_word = max(wordfreq)
    word = word_sort[wordfreq.index(max_word)] # <--- solution!


    result = word

    return result


def test_run():
    """Test most_frequent() with some inputs."""
    print(most_frequent("london bridge is falling down falling down falling down london bridge is falling down my fair lady")) # output: 'down'
    print(most_frequent("betty bought a bit of butter but the butter was bitter")) # output: 'butter'
    print(most_frequent("a a a a b b b b")) #output: 'a'
    print(most_frequent("z z j j z j z j")) #output: 'j'

test_run()