# strings
print("hello there")
print("hello")

# Assign String to a Variable
a = 'hello'
print(a)

# Multiline Strings

a = """" 
there is
 a multiline
   string
   """

print(a)


# three single quotes
a = ''' Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua'''
print(a)

# strings arrays
a = "hello world"
print(a[1])


# Looping Through a String
for x in "banana":
  print(x)


  # string length
a = "hello world"
print(len(a))


# check string
txt = " the best thing in life are free"
print("free" in txt)


# Use it in an if statement:


txt = "that is the way in your life"
if "way" in txt:
  print('yes  "way" is the present')


  # Check if NOT
  txt = "the best things in life are free"
  print("expensive" not in txt)


  if "expensive" not in txt:
    print('no "expensive" is not present ')