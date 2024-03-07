import random
import string

def generate_random_color_hex():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def generate_random_alphabetical_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def generate_random_integer_between(min_value, max_value):
    return random.randint(min_value, max_value)

def generate_random_multiple_of_7():
    return random.choice(range(0, 71, 7))

random_color_hex = generate_random_color_hex()
random_alphabetical_string = generate_random_alphabetical_string(8)
random_integer = generate_random_integer_between(10, 20)
random_multiple_of_7 = generate_random_multiple_of_7()

print("Random Color Hex:", random_color_hex)
print("Random Alphabetical String:", random_alphabetical_string)
print("Random Integer between 10 and 20:", random_integer)
print("Random Multiple of 7 between 0 and 70:", random_multiple_of_7)
