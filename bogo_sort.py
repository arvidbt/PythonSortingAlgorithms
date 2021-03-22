import random

elements_sorted = False
elements = [int(x) for x in input().split(" ")]

while not elements_sorted:
    random.shuffle(elements)
    print(elements)
    if(elements == sorted(elements)):
        elements_sorted = True
        
print(elements)