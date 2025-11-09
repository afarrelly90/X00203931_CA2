# basic calculator application

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multi(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ValueError('Cant divide by zero.')
    return a / b