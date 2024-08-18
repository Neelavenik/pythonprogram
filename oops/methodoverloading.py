from multipledispatch import dispatch
class Maths():
    @dispatch(int,int)
    def add(self,a,b):
        self.a=a
        self.b=a
        print(a+b)
    @dispatch(int,int,int)
    def add(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        print(a+b+c)
ob1=Maths()
ob1.add(10,20)