class car():
    def __init__(self,name,model):
        self.name=name
        self.model=model
    def move(self):
        print("drive slowly")
class boat():
    def __init__(self,name,model):
        self.name=name
        self.model=model
    def move(self):
        print("sail the boat")
class plane():
    def __init__(self,name,model):
        self.name=name
        self.model=model
    def move(self):
        print("fly in the sky")
car1=car('BMW','pro')
boat1=boat('steamer','navy')
plane1=plane('emarades','latest')
car1.move()