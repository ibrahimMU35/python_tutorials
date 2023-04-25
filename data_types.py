# Python has the following data types built-in by default, in these categories:
# text type = str
# numeric types = int, float, complex
# sequence types = list, tuple, range
# mapping type = dict
# set types = set, frozenset
# boolean type = bool
# binary types = bytes, bytearray, memoryview
# none type = NoneType


# getting data type
x = 5
print(type(x))



# data type str
x = "hello world"

print(x)

print(type(x))

# data type int
x = 20
print(x)
print(type(x))

# data type float

x = 20.5

print(x)
print(type(x))

# data type complex
x = 1j
print(x)
print(type(x))

# data type list

x = ["apple", "orange","banana"]
print(x)
print(type(x))

# data type tuple
x = ("cherry", "banana", "apple")
print(x)
print(type(x))

# data type range
x = range(6)
print(x)
print(type(x))

# data type dict
x = {"name":"jhon" , "age":32}

print(x)
print(type(x))

# data type set
x = {"apple", "cherry", "banana"}
print(x)
print(type(x))

# data type frozenset
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

# data type bool
x = True 
print(x)
print(type(x))

# data type bytes
x = b"hello"
print(x)
print(type(x))

# data type bytearray
x = bytearray(5)
print(x)
print(type(x))

# data type memoryview
x = memoryview(bytes(5))

print(x)
print(type(x))

# data type NoneType
x = None
print(x)
print(type(x))
