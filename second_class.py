class SoliderInfo:
    def __init__(self):
        self.hp = 0
        self.attack = 0

class Weapon:
    def __init__(self):
        self.name = "no"

class Solider: 
    def __init__(self, setSoliderInfo, setWeapon):
        self.soliderInfo = setSoliderInfo #self.自己取名(通常都小寫)->變數變屬性
        self.weapon = setWeapon
    
    def beat(self, power):
        self.soliderInfo.hp -= power 

    def get_weapon_name(self):
        return self.weapon.name

soliderInfo1 = SoliderInfo()
soliderInfo1.attack = 10
soliderInfo1.hp = 8

arrow= Weapon()
arrow.name = "ARROW"

solider1 = Solider(soliderInfo1,arrow)

solider1.beat(11)
print(solider1.soliderInfo.hp)
print(solider1.get_weapon_name()) #1. return的出來
print(solider1.weapon.name) #2. 直接印屬性