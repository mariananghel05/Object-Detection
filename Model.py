
class Model:
    
    def __init__(self, Name = None, Model = None):
        self.Model = {}

        if Name != None  or  Model != None:
            self.Model[Name] = Model 
    
    def add(self, Name, Model):
        self.Model[Name] = Model
    
    def delete(slef, Name):
        slef.Model.pop(Name)






