#import math
#print(math.sqrt(16))


######function####
def greet():
    print("Hello, World!")
greet()


###defining a function with parameters###
def add_numbers(a,b):
    return a + b
result = add_numbers(5, 3)
print("The sum of 5 and 3 is:", result)

###local vs global variable###
x= 10
def show_value():
    x = 5
    print(x)
show_value()
print(x)

###importing modules###
import math
import random
print(math.sqrt(16))
print(random.randint(1, 10))


###shared variable example###
icecream = "vanilla"
vegetable = "carrot"
def food():
    fruit = "apple"
    print(fruit,"is good for health")
    print(icecream,"is a good flavour")
food()
print("Vegetable is also good for health:", vegetable)


import random
print(random.uniform(1, 25))