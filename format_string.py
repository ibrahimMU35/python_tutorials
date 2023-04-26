# ----String Format-----


# age = 35
# txt = "my name is  jhon , I am " + age 
# print(txt)

# TypeError: can only concatenate str (not "int") to str


# Use the format() method to insert numbers into strings:
age = 35
txt = "my name is jhon, i am  {} years old"
print(txt.format(age))

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:k


quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))