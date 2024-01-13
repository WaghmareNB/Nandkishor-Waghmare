class A:
    a=10
    def get(self):
        print("hi")

class B(A):
    b=20
    def show(self):
        print("Hellow")

obj=B()
obj.get()
obj.show()