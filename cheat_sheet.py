import math
# this is where i mess around with stuff.
print("Hello, World.")

# variables
students_count = 1000
rating = 4.99
is_published = False
course_name = "Python Programming"
print(students_count)

message = """To Whom This May Concern,

Congratulations on your new job."""
length_of_message = len(message)
print(length_of_message)
print(message[10])
print(message[0:10])
print(message[0:])
print(message[:9])

first = "Hugo"
second = "Otto"
full = f"{first} & {second}"
print(full)

print(full.upper())
print(full.lower())
print(full.title())
print(full.find("Otto"))
print(full.replace("o", "k"))
print("to" in full)

print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

x = 10
print(x)
x = x+3
print(x)
x = 10
x += 3
print(x)

print(math.ceil(2.2))
