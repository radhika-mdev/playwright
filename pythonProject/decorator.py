def add(a,b):
    return a+b

def calculate(add,a,b):
    return add(a,b)

result=calculate(add,2,3)
print(result)


def greeting(name):
    def hello():
        return "hai,goodmng"+name
    return hello

greet=greeting("Radhika")
print(greet())

def greeting(name):
    def hello():
        return "Hello, " + name + "!"
    return hello

greet = greeting("Atlantis")
print(greet())  # prints "Hello, Atlantis!"

# Output: Hello, Atlantis!

def decfunc(func):
    def inner():
        print("decorated function")
        func()
    return inner

@decfunc
def origfunc():
    print("this is original function")


origfunc()

def calc(func):
    def inner(a,b):
        print("decorated function")
        return func(a,b)
    return inner

@calc
def sum(a,b):
    print(a+b)


sum(5,2)



