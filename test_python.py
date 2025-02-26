x = 5  # global variable
y = 6

def outer():
    x = 10  # enclosing function variable

    def inner():
        nonlocal x  # Modify the variable in the enclosing scope
        x = 20  # Modify x in outer() function

        global y  # Declare y as a global variable
        y = 30  # Modify the global variable y

    print("outer x",x)  # Output: 10 (defined in outer function)
    print("outer y",y)  # Output: 6  (this is from the main)
    inner()
    print("after inner x",x)  # Output: 20 (modified by nonlocal)
    print("after inner y",y)  # Output: 30 (modified by global)

outer()

print("main x",x)  # Output: 5 (not affected by nonlocal change)
print("main y",y)  # Output: 30 (modified by global)
