# import sys
# sys.path.insert(1,"C:\\Users\\manishk\\Desktop\\practice")
import cars.tesla
# import cars.name1
# import gym.chest 
# import gym.legs
import cars.bmw
import argparse
parser=argparse.ArgumentParser()
parser.add_argument("bmw_model",type=str)
parser.add_argument("tesla_model",type=str)
parser.add_argument("chest_machine_name",type=str)
parser.add_argument("legs_machine_name",type=str)
args=parser.parse_args()
def fn():
    return args.bmw_model,args.tesla_model,args.chest_machine_name,args.legs_machine_name
# fn()
# def fn():
#     return args.bmw_model
# fn("bmw type")

# print(f"package creation was successul for gym")
# print(chest.chest().chest())
# print(gym)