class A:
    def doA(self):
        print("do A")


class B:
    def doB(self):
        print("do B")


class C:
    def doC(self):
        print("do C")


class D(A, B, C):
    def doD(self):
        print("do D")

    def all(self):
        self.doA()
        self.doB()
        self.doC()
        self.doD()


d = D()
print()
d.doA()
print()
d.doD()
print()
d.all()
