def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")
# Expected output:
# Age: 35, Height: 74, Weight: 180, IQ: 50

# Actual output:
# Age: 35, Height: 74, Weight: 180, IQ: 50.0

# A puzzle for extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

# -4391  -4426  4500  25

print("That becomes: ", what, "Can you do it by hand?")
# Expected output:
# That becomes: -4391 Can you do it by hand?

# Actual output:
# That becomes: -4391 Can you do it by hand?
