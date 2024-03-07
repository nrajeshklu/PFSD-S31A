import random
from datetime import datetime, timedelta

def generate_random_integer_excluding(max_value):
    return random.randint(0, max_value - 1)
def generate_random_integer_range_excluding(min_value, max_value):
    return random.randint(min_value, max_value - 1)
def generate_random_integer_with_step(start, end, step):
    return random.randrange(start, end, step)
def generate_random_date(start_date, end_date):
    time_delta = end_date - start_date
    random_days = random.randint(0, time_delta.days)
    return start_date + timedelta(days=random_days)

random_int_excluding_6 = generate_random_integer_excluding(6)
random_int_range_excluding_10 = generate_random_integer_range_excluding(5, 10)
random_int_with_step = generate_random_integer_with_step(0, 10, 3)
start_date = datetime(2022, 1, 1)
end_date = datetime(2022, 12, 31)
random_date = generate_random_date(start_date, end_date)

print("Random Integer between 0 and 6 (excluding 6):", random_int_excluding_6)
print("Random Integer between 5 and 10 (excluding 10):", random_int_range_excluding_10)
print("Random Integer between 0 and 10 with a step of 3:", random_int_with_step)
print("Random Date between {} and {}: {}".format(start_date, end_date, random_date))
