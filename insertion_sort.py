elements = [int(x) for x in input().split(" ")]

for i in range(1, len(elements)):
    
    pivot = elements[i]
    j = i - 1

    while j >= 0 and pivot < elements[j]:
        elements[j + 1] = elements[j]
        j -= 1

    elements[j + 1] = pivot

print(elements)