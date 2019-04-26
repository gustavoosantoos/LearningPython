def myFunction():
    print("Testing")

myFunction()

def myFuntionWithParameters(x):
    print(x)

myFuntionWithParameters("Hello Functions")

def myFuntionWithDefaultParameters(x = "Hello default params"):
    print(x)

myFuntionWithDefaultParameters()
myFuntionWithDefaultParameters("Hello Functions")

def functionWithReturn(x = 1):
    return 10 * x

print(str(functionWithReturn(3)))

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(str(factorial(998)))