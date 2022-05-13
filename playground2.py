# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args):
        a = 1
        for i in args:
            a = a * i
        return print(f"You called {function.__name__}{args} \n It returned: {a}")
    return wrapper

# Use the decorator 👇
@logging_decorator
def a_function(*args):
    return args

@logging_decorator
def b_function(*args):
    return args


a_function(1, 2, 3)
b_function(1, 2, 3, 4)