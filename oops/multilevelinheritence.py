class grandparent():
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
class parent(grandparent):
    def __init__(self,occupation,name,gender):
        super().__init__(name,gender)
        self.occupation=occupation
class child(parent):
    def __init__(self,age,name,gender,occupation):
        super().__init__(occupation,name,gender)
        self.age=age

    def show(self):
        print(self.name)
        print(self.gender)
        print(self.occupation)
        print(self.age)
ob1=child(20,'neelu','female','software')
ob1.show()