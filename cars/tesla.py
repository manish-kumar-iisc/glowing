import sys
sys.path.insert(1,"C:\\Users\\manishk\\Desktop\\practice")
# from name_global import fn

class tesla:
    def __init__(self,model_type):
        # print("tesla class called")
        self.model_type=model_type
        return
    
    def tesla(self):
        print(f"class is {__name__} and type is {self.model_type}")


# value=list(fn())
value="no"
obj=tesla(value[1])
obj.tesla()