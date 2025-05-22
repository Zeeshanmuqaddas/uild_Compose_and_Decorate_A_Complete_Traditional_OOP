class A:
    def show(self):
        print("Show from A")

class B(A):
    def show(self):
        print("Show from B")

class C(A):
    def show(self):
        print("Show from C")

class D(B, C):
    pass

# Create an object of D
d = D()
d.show()  # Observe MRO

# Print the Method Resolution Order
print(D.__mro__)
