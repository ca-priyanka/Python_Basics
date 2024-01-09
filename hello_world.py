print("Hello World")
print("hello Python World")
message = "Hello Python World"
print(message)
message = "hello crash course world"
print(message)
name = "priyanka bhatnagar"
print(name.title())
print(name.upper())
first_name = "priyanka"
last_name = "bhatnagar"
# Use f for formatting strings
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()} !")
# Use t for giving a tab to string
print("\tPython")
# \n is used to add a newline in a string
print("Languages:\nPython\nC\nJavaScript")
# stripping whitespace
favourite_language = 'python '
favourite_language.rstrip()
# strip whitespace from leftside of the string using lspace or bothsides using strip
favourite_language = ' python '
favourite_language.strip()
# Removing prefix or removesuffix
nonstarch_url = 'https://nonstarch.com'
nonstarch_url.removeprefix('https://')
# you can write _ in integers to make it more readable, python ignores the unerscore while printing
universe_age = 14_000_000_000
print(universe_age)
# multiple assignment - makes your code shorter
x,y,z = 1,2,3
print(x)
# constants-a variable in all capital letters is treated as constant
MAX_CONNECTIONS = 5000

