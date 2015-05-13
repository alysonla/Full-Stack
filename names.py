# Open names.txt file

# Write a Python script which loads the names from the file, and converts your own name to a
# superhero (or supervillain) name by picking the name corresponding to your first name's position
# in the alphabet (there are 26 superheroes in the list). For example, if your name starts with A,
# you want superhero name #1. Mine (J) is name #10.

with open('names.txt') as f:
    data = f.readlines()

    # for name in data:
    #     print name.strip()



# Figure out how to put all in list & access the list

# Here's a snippet of code to help with the letter part of this:

import string
uppers = string.uppercase
# print uppers  # this will help you figure out what this is
a_position = uppers.find('A')  # .find shows you what position the letter is in.
print a_position

print data[a_position].strip()
