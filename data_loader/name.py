import sys
sys.path.insert(1,"C:\\Users\\manishk\\Desktop\\practice")
from cars import bmw
import cars.tesla
import cars.name1
# print(f"package creation was successul for cars")
import gym.chest as chest
import gym.legs
import cars.bmw
import argparse
parser=argparse.ArgumentParser()
parser.add_argument("bmw_model",type=str)
parser.add_argument("tesla_model",type=str)
parser.add_argument("chest_machine_name",type=str)
parser.add_argument("legs_machine_name",type=str)
args=parser.parse_args()
# def fn():
#     return args.bmw_model
# def fn():
#     return args.bmw_model
# fn("bmw type")

# print(f"package creation was successul for gym")
# print(chest.chest().chest())
# print(gym)