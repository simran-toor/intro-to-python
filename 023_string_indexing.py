# In the earlier material, we focused on numbers.

# Numbers are a very simple data type — they represent a
# single value.

# Strings are more complex. They're a basic form of what, in
# programming, we call a 'data structure'.

# This means they've got more than one thing in them, and
# they're organised in a specific way depending on what type
# of data structure they are.

# A string has a number of characters inside it in a
# particular order.

# Take this string:

note = "The Most Perfect Crab"
print(note)

# We can access the first character like this:

print(note[0])
# In programming, we count from zero — 'T' is the zeroth
# character.

# And the last character like this:

print(note[-1])

# And any in the middle like this:

print(note[6])

# You can also get a 'slice' of the string like this:

print(note[0:3])
# This gets the portion of the string between index 0 and 3:
# 'The'

# @TASK: Complete the following exercises. You can check
# them as you go by running: python 023_string_indexing.py

# == Exercise One ==

print("")
print("Function: get_first_letter")

def get_first_letter(string):
  # Return the first letter of the string
  return(string[0])

print(get_first_letter("The king granted them"))
print(get_first_letter("Five years later"))

# == Exercise Two ==

print("")
print("Function: get_last_letter")

def get_last_letter(string):
  # Return the last letter of the string
  return(string[-1])

print(get_last_letter("The king granted them"))
print(get_last_letter("Five years later"))

# == Exercise Three ==

print("")
print("Function: get_nth_letter")

def get_nth_letter(string, n):
  # Return the letter of the string at the specified index
  return(string[n])

print(get_nth_letter("The king granted them", 4))
print(get_nth_letter("Five years later", 7))

# == Exercise Four ==

print("")
print("Function: get_letters_between_four_and_eight")

def get_letters_between_four_and_eight(string):
  # Return the section of the string between indexes four
  # and eight
  return(string[4:8])

print(get_letters_between_four_and_eight("The king granted them"))
print(get_letters_between_four_and_eight("Five years later"))
