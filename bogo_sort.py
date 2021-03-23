import random

elements_sorted = False
iteration = 0
elements = [int(x) for x in input().split(" ")]

while not elements_sorted:
    random.shuffle(elements)
    print(iteration, elements)
    if(elements == sorted(elements)):
        elements_sorted = True
    iteration += 1

print("Number of tries to sort list: " + str(iteration))
print(elements)