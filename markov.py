from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text = open(file_path).read()

    return text

# print open_and_read_file('green-eggs.txt')   


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}
    words = text_string.split()

    dict_value = []

    for i in range(len(words)-2):

        key = (words[i], words[i+1])
        value = words[i+2]
        values = chains.get(key, [])
        values.append(value)
        chains[key] = values

    return chains

def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
    # import random generator
    # have random generator pick a starting point
    # random generator will pick a random tuple
    # get random item in the list associated with the random tuple
    #  shift the key by 1
    # get a random value associated with the new key
    # if the word None appears in the loop, then stop
    import random
    key_list = chains.keys()
    first_key = random.choice(key_list)
    random_value = chains.get(first_key)
    first_value = random.choice(random_value)

    # create the first string and update with the new strings generated after
    new_string = ' '.join(first_key) + ' ' + first_value + ' '

    next_key = first_key[1]
    new_key = (next_key, first_value)

    while True:
        # gets the value (a list) associated with the new key from line 65
        next_key_list = chains.get(new_key) 
        # get random value from the list in 71
        # print "next_key_list", next_key_list
        next_value = random.choice(next_key_list)
        # print "next_value", next_value
        # creates the next new key 
        new_key = (new_key[1], next_value)
        # print "new_key", new_key

        new_string += next_value + ' '

        if chains.get(new_key) is None:
            break

    return new_string        


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
