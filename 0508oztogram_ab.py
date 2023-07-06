from abc import abstractmethod

class OzToGram:   
    @abstractmethod
    def oz_to_gram(self,oz):
        pass

class Gold(OzToGram):
    def oz_to_gram(self,oz):           
        self.gram=oz*31
        return self.gram

class Normal(OzToGram):
    def oz_to_gram(self,oz):
        self.gram=oz*28
        return self.gram

sth= Gold()
x = sth.oz_to_gram(20)
print(x)

if x>600:
    print("x>600")
else :
    print("x<600")
    