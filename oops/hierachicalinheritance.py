class Animal():
    def __init__(self,color,tail,legs):
        self.tail=tail
        self.color=color
        self.legs=legs
class cat(Animal):
   def show(self):
       print(self.tail)
       print(self.color)
       print(self.legs)
       print("animal cat")
class dog(Animal):
    def show(self):

        print(self.color,self.tail,self.legs)

        # print(self.tail)
        # print(self.color)
        # print(self.legs)
        print("animal dog")
ob1=dog('brown',1,4)
ob1.show()
ob2=cat('white',1,4)
ob2.show()
