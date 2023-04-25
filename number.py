# there are 3 numeric types in python

"""
int, float , complex
"""

x = 1
print(x)
print(type(x))

x = 2.8
print(x)
print(type(x))

x = 2j
print(x)
print(type(x))

# int

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

# Float
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))




x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))





# Complex
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))





# Type Conversion
# You can convert from one type to another with the int(), float(), and complex() methods:


x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)
print(a)
print(type(a))

# convert from float to int 
b = int(y)
print(b)
print(type(b))

# convert from int to complex:
c = complex(x)
print(c)
print(type(c))

# convert from foat to complex
u = complex(y)
print(u)
print(type(u))



# random numbers 
import random
print(random.randrange(1,10))