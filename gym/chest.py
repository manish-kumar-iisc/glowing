import sys
sys.path.insert(1,"C:\\Users\\manishk\\Desktop\\practice")
from name_global import fn
class chest:
    def __init__(self,exercise_type):
        self.list1=["lat pull down", "multi press", "butter fly", "cross cabel","dumbel press"]
        
    def chest(self):
        # print(f"excercises for chest are{self.list1}")
        # return self.list1
        print(__name__,self.list1[0])

value=list(fn())
obj=chest(value[2])
obj.chest()
# chest().chest()