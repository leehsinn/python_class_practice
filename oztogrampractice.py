class OzToGram:
    def __init__(self,type):
        print("start to calculate")
        if type==1:
            self.__con=31.1 #把原先的self.con封裝
        elif type==2:
            self.__con=28.35
        else:
            print("wrong")    

    def get_con(self): #讀取封裝
        return self.__con

    def result(self,oz): 
        return oz*self.__con
    
sth= OzToGram(2)
ans=sth.result(20)
print(ans)

print(sth.get_con()) #顯示封裝
