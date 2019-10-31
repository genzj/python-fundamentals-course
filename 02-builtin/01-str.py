# -*- encoding: utf-8 -*-
# Strings are created with " or '

#########################
#   Basic operations
#########################
"This is a string."
'This is also a string.'

# Strings can be added too! But try not to do this.
"Hello " + "world!"  # => "Hello world!"
# String literals (but not variables) can be concatenated without using '+'
"Hello " "world!"    # => "Hello world!"

"Hello " * 3 # => "Hello Hello Hello "

# You can find the length of a string
len("This is a string")  # => 16

# Substring existence
"a" in "abc" # => True

# Substring location
'abc'.find('bc') # => 1
'abc'.find('d') # => -1

# Substitution
'abxd'.replace('x', 'c') # => 'abcd'


#########################
#      Formatting
#########################

# like printf in C
print("My name is %s and weight is %d kg!" % ('Zara', 21) )

# but not limited to printing
"%s can be %s the %s way" % ("Strings", "interpolated", "old")  # => "Strings can be interpolated the old way"

# .format can be used to format strings, like this:
"{} can be {}".format("Strings", "interpolated")  # => "Strings can be interpolated"

# You can repeat the formatting arguments to save some typing.
"{0} be nimble, {0} be quick, {0} jump over the {1}".format("Jack", "candle stick")
# => "Jack be nimble, Jack be quick, Jack jump over the candle stick"

# You can use keywords if you don't want to count.
"{name} wants to eat {food}".format(name="Bob", food="lasagna")  # => "Bob wants to eat lasagna"


#########################
#  Indexing / slicing
#########################
# A string can be treated like a list of characters
"abc"[1] # => "b"
"abc"[-1] # => "c"

"abcd" [0:2] # => "ab"
"abcd" [0::2] # => "ac"
"abcd" [-1::-1] # => "dcba"
