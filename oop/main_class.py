class Parent:
    def __init__(self):
        self.name = "GrandParent"
        print(self.name)
        type(self)

class SuperChild(Parent):
    def __init__(self):
        super().__init__()
        self.name = "SuperChild"
        print(self.name)

class GrandChild(SuperChild):
    def __init__(self):
        super().__init__()
        self.name = "GrandChild"
        print(self.name)


print(GrandChild())