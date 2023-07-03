def decorator1(func):
    def wrapper(*args, **kwargs):
        print("enter decorator1")
        response = func(*args, **kwargs)
        print("exit decorator")
        return response
    return wrapper

def decorartor2(func):
    def wrapper(*args,**kwargs):
        print("enter decorator2")
        response = func(*args, **kwargs)
        print("exit decorator2")
        return response
    return wrapper()

# @decorartor2(7)
