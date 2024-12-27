import logging

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated
  
# def greet(func):
#   def mfx(*args, **kwargs):
#     print("Good Morning")
#     func(*args, **kwargs)
#     print("Thanks for using our service")
#   return mfx
    
# def greeting(func):
#   def mfx():
#     print("Good Morning")
#     func()
#     print("Have a nice day")
#   return mfx

# def _greeting(func):
#   def mfx(*args):
#     print("Hello")
#     func(*args)
#     print("Have a nice day")
#   return mfx
  

# @greeting # First way of decorator
# def printName():
#   print("Hello! sir")

# printName()
# print()
# greeting(printName)() # Second way of decorator


# print()


# @_greeting
# def printName(name):
#   print(f"{name}")
  
# printName("Basu")
# print()
# _greeting(printName)("Sonu")


# print()


# @greet
# def addTwoNumber(a,b):
#   print(a+b)
  
# addTwoNumber(3,4)
# print()
# greet(addTwoNumber)(5,15)




@log_function_call
def my_function(a, b):
    return a + b
  
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
  
print(my_function(5, 10))