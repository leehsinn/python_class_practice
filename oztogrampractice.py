class OzToGram:
    def __init__(self,type):
        print("start to calculate")
        if type==1:
            self.con=31.1
        elif type==2:
            self.con=28.35
        else:
            print("wrong")    


    def result(self,oz): 
        return oz*self.con
    
sth= OzToGram(2)
ans=sth.result(20)
print(ans)
print(sth.con)
sth.con=10
print(sth.con)
