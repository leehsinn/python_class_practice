class Bird:
    def set_name(self, name):
        print("name is "+name)
    def is_fly(self, canfly):
        if canfly:
            print("I can fly")
        else:
            print("I cannot fly")

duck= Bird()
duck.set_name("duck1")
duck.is_fly(False) #直接放bool值



def set_name_function(name):
    print("name is "+name)
    
    return name


final=set_name_function("hsin")
print(final)