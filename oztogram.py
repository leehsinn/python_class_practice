class OzToGram:
    def gold_oz(self,oz):
        gram=oz*31.1
        print("gold is "+str(gram))
    
    def normal_oz(self,OZ):
        Gram=OZ*28.35
        print("it is "+str(Gram))

sth= OzToGram()
sth.gold_oz(20)
sth.normal_oz(20)
    