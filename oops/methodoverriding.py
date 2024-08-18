class parent():
    def __init__(self):
        self.value="parent class"
    def display(self):
        print(self.value)
class child(parent):
    def __init__(self):
        super().__init__()
        self.value="child class"

    def display(self):
        print(self.value)
ob1=child()
ob1.display()
ob2=parent()
ob2.display()