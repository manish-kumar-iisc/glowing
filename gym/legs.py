import sys
sys.path.insert(1,"C:\\Users\\manishk\\Desktop\\practice")
from name_global import fn
class legs:
    def __init__(self,exercise_type):
        self.list1=["leg press"]
        return
        # print(f"excercises for chest are{self.list1}")
    def legs(self):
        # path=os.path.abspath(__file__)
        print(__name__, self.list1[0])
        # return self.list1

value=list(fn())
obj=legs(value[3])
obj.legs()