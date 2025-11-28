a = input("Enter value for a: ")
b = input("Enter value for b: ")
c = input("Enter value for c: ")

print("Before swapping:")
print("a =", a, "b =", b, "c =", c)

a, b, c = c, a, b

print("After swapping:")
print("a =", a, "b =", b, "c =", c)