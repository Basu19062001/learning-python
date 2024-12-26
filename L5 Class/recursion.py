def factorial(n):
  if(n==0 or n==1):
    return 1
  else:
    return n*factorial(n-1)
print(factorial(6))

def fact(n):
  return 1 if n in [0,1]  else n*fact(n-1)
print(fact(6))


def fibonacci(n):
  if(n==0):
    return 0
  elif(n==1):
    return 1
  else:
    return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(6))

def fib(n):
  return 0 if n==0 else 1 if n==1 else fib(n-1)+fib(n-2)
print(fib(6))  