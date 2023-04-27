# Python Booleans
# Booleans represent one of two values: True or False.

print(10 > 9)
print(10 == 9)
print(10 < 9)


# Print a message based on whether the condition is True or False
a = 200 
b = 44 

if b>a:
    print("b is greater than a")
else:
    print("b is less than a")


    # The bool() function allows you to evaluate any value, and give you True or False in return,
print(bool("Hello"))
print(bool(15))
print(bool(0))



x = "Hello"
y = 15

print(bool(x))
print(bool(y))


print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))


# Some Values are False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))



class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))



# Functions can Return a Boolean
def myFunction() :
  return True

print(myFunction())




def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

  # Check if an object is an integer or not:
x = 200
print(isinstance(x, int))