#With this concept of default parameters in mind,
#the goal of this assignment is to write a single function, randInt() that takes up to 2 arguments.
import random
def randInt(min=0,max=100):
    if min > max:
        print("Min can't be greater than max.")
        return
    elif max < 0:
        print("Max is negative!!!.")
        return
    num = random.random() * (max - min) + min
    return round(num)
#If no arguments are provided, the function should return a random integer between 0 and 100.
print(randInt())
#If only a max number is provided, the function should return a random integer between 0 and the max number.
print(randInt(max=50)) 
#If only a min number is provided, the function should return a random integer between the min number and 100
print(randInt(min=50))
#If both a min and max number are provided, the function should return a random integer between those 2 values.
print(randInt(min=50, max=500))
