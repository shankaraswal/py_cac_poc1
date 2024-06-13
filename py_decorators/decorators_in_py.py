# decorators are like HOC

import time


def timer(fn):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        end = time.time()
        print(f"{fn.__name__}() funciton time-taken : ", end - start)
        return result
    return wrapper


@timer
def add(a, b):
   return a + b

@timer
def greet(name, greet):
    return(f"{greet} {name}")
    
print(add(5,12))
print(greet('hiya','shan'))