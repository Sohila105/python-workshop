import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIMER] '{func.__name__}' executed in {end - start} seconds")
        return result
    return wrapper

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOGGER] Calling '{func.__name__}' with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOGGER] '{func.__name__}' returned {result}")
        return result
    return wrapper

def count_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper

def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[DEBUG] Function '{func.__name__}'")
        print(f"   args: {args}")
        print(f"   kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"   returned: {result}")
        return result
    return wrapper

#test
@timer
def slow_function(n):
    time.sleep(n)
    return f"Slept for {n} seconds"


result = slow_function(2)
print(result)

@logger
def add(a, b):
    return a + b
result = add(5, 3)


@count_calls
def greet(name):
    return f"Hello, {name}!"
greet("Alice")
greet("Bob")
greet("Charlie")
print(f"Total calls: {greet.call_count}")

@debug
def calculate_average(numbers):
    return sum(numbers) / len(numbers)
result = calculate_average([10, 20, 30, 40])


@timer
@logger
def multiply(x, y):
    return x * y
result = multiply(4, 5)