from abc import abstractmethod #多型

class Soilder:
    @abstractmethod #多型
    def who_you_are(self):
        pass

class Healer(Soilder):
    def who_you_are(self):
        return "I am Healer"

class Archer(Soilder):
    def who_you_are(self):
        return "I am Archer"
    
xSoilder = Archer() #或更換 Healer()
print(xSoilder.who_you_are())