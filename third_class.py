class Solider: #父
    def __init__(self, setHp, setAttack):
        self.hp = setHp
        self.attack = setAttack
    
    def beaten(self, power):
        self.hp -= power 

class Archer(Solider): #子(繼承父的method-->beaten)
    def attack_by_arch(self):

        return self.attack

class Healer(Solider): #子
    def heal_myself(self):
        self.hp+=5
        return self.hp
    
    def heal_other(self,setArcher):
        self.archer=setArcher
        self.archer.hp+=3
        return self.archer.hp
    
alex = Archer(11,24)
print(alex.attack_by_arch())
alex.beaten(10)
print(alex.hp)

angel = Healer(11,20)
angel.beaten(10)
print(angel.heal_myself())
print(angel.heal_other(alex))
print(alex.hp) #double check
