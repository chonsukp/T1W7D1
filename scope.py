# Scope - global and local

fname = "Pat"
lname = "Cummins"

# Control flow statement - Outside of function will print first

# Pure function
def greet():
    fname = "Steven"
    lname = "Smith"
    print("Inside the function")
    print(fname)
    print(lname)

print("Outside the function")
print(fname)
print(lname)
greet()