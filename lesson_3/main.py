import json
def decorator(func):
    def wrapper(user:dict):
        if user['role'] <= "ADMIN":
              return func(user)

    return wrapper

@decorator
def print_user(user:dict):
    return user['role'],user['name']

with open("users.json",'r')as f:
        for user in json.load(f):

            response = print_user(user)
            if response:
                print(response)