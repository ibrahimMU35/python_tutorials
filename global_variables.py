# Global Variables


# Create a variable outside of a function, and use it inside the function

x = "science"

def myfunc():
  print(x + " is game changer")


myfunc()

# Create a variable inside a function, with the same name as the global variable


x = "awesome" 
def myfunc():
  x = 'fantastic'
  print('python is  ' + x)

myfunc()

print('python is ' + x)

# global keyword

# If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x  
  x = 'scientist'

myfunc()

print('python is ' +  x)


# To change the value of a global variable inside a function, refer to the variable by using the global keyword:

y = 'spectaculer'

def myfunc():
  global y
  y = 'awesome'
  print('python is ' +y)

myfunc()  

print('python is ' + y)


