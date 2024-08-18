class parent():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
class child(parent):
    def display(self):
        print(self.name)
        print(self.age)
        print(self.gender)

ob1=child('neelu',25,'female')
ob1.display()