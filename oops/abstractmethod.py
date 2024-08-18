from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def Color(self):
        ...


    @abstractmethod
    def Model(self):
        ...

    @abstractmethod
    def speed(self,kmph):
        ...


class car(Vehicle):
    def Color(self,color):
        self.color=color
        print(self.color)
    def Model(self,model):
        self.model = model
        print(self.model)
    def speed(self,kmph):
        self.kmph = kmph
        print(self.kmph)
    def execute(self):
        print("welcome to bmw")

ob1=car()
ob1.Model(746)
ob1.Color('white')
ob1.speed('70kmp')
ob1.execute()