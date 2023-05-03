class Bird:
    def set_name(self,name):
        print("name is"+name)


def set_name_function(name):
    print("name is "+name)
    
    return name


final=set_name_function("hsin")
print(final)