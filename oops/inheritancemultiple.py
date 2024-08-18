#child class inherits properties from more thsn one parent class
class A():
    def method1(self,name):
        self.name=name
        print('parent1')
        print(self.name)
class B():
    def method2(self,age):
        self.age=age
        print('parent2')
        print(self.age)
class child(A,B):
    def method3(self,gender):
        self.gender=gender
        print("child class")
        print(self.gender)
obj=child()
obj.method3('female')
obj.method2('20')
obj.method1('neelu')