class ABC:
    n=int(input("Enter any Number"))
    def show(self):
        if self.n>0:
            print("no is positive")
        else:
            print("no is negative")

obj=ABC()
obj.show()