import argparse
import os
import random

#Random fruits list
random.seed(42)
fruits = ["Apple", "Banana", "Peach", "Kiwi", "Pear ", "Tomato", "Plum"]
length = 10000000

#Command-line arguments parser
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--ListLength", help = "Length of the desired fruits list")

#Parse arguments
args = parser.parse_args()
if args.ListLength:
    length = int(args.ListLength)

#Print random list to file
dir_path = os.path.dirname(os.path.realpath(__file__))
with open(f"{dir_path}/fruitList.txt","w") as f:
    for _ in range(length):
       index = random.randint(0,len(fruits)-1)
       f.write(fruits[index]+'\n')