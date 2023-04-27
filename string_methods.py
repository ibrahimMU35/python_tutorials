# string methods
# Note: All string methods return new values. They do not change the original string.

  # capitalize()	Converts the first character to upper case
txt = 'hello there'
print(txt.capitalize())
# The first character is converted to upper case, and the rest are converted to lower case
txt = "python is FUN"
print(txt.capitalize())
# See what happens if the first character is a number:
txt = "36 is my age."

x = txt.capitalize()

print (x)

# casefold()	Converts string into lower case

txt = "HELLO WORLD"
print(txt.casefold())


# center()	Returns a centered string
# Print the word "banana", taking up the space of 20 characters, with "banana" in the middle:

txt = "banana"
print(txt.center(20))
# Using the letter "O" as the padding character:
print(txt.center(20,"O"))



# count()	Returns the number of times a specified value occurs in a string
txt = "i love apple, i eat an apple ,i prefer an apple ,i like apple"
print(txt.count("apple"))


# Search from position 10 to 24:
txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple", 10, 24)

print(x)




# encode()	Returns an encoded version of the string
# UTF-8 encode the string:
txt = "My name is Ståle"

x = txt.encode()

print(x)









# Method	Description
# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning