class Cat:
    #constructor ham khoi tao
    def __init__(self,name,weight):
        self.name=name
        self.weight=weight
    def run(self):
        #do something
        print("Cat %s is running"%(self.name))

    #getter and setter
    def set_name(self,new_name):
        self.name=new_name
    def get_name(self):
        return self.name

Cat1=Cat(name="vien",weight=55)
print(Cat1)
#bat dau voi class