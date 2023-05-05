class Solider: #通常第一個字大寫

    def __init__(self, setHp, setAttack):
        self.hp = setHp
        self.attack = setAttack
    
    def beat(self, power):
        self.hp -= power #self.hp=self.hp-power
    
    def is_a_live(self): #*如果方法沒有需要使用變數，不用召喚
        if self.hp>0:
            return True
        return False #精簡寫法

soilder1 = Solider(10,5)

soilder1.beat(11)
print(soilder1.hp)
fin=soilder1.is_a_live() #*上面沒召喚下面不用填
print(fin)