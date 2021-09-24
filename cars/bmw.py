import sys
sys.path.insert(1,"C:\\Users\\manishk\\Desktop\\practice")
from name_global import fn

class bmw:
    def __init__(self,model_type):
        self.model_type=model_type
        return
        # print("bmw yes")
        # print(__name__)
    def bmw(self):
        print(f"class is {__name__} and type is {self.model_type}")


value=list(fn())
obj=bmw(value[0])
obj.bmw()