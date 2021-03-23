def partition(elements, low, high):
    i = low - 1
    pivot = elements[high]

    for j in range(low, high):
        if elements[j] <= pivot:
            i = i+1
            elements[i], elements[j] = elements[j], elements[i]

    elements[i+1], elements[high] = elements[high], elements[i+1]
    return i+1


def quick_sort(elements, low, high):
    if len(elements) == 1:
        return elements
    if low < high:
        pivot = partition(elements, low, high)

        quick_sort(elements, low, pivot-1)
        quick_sort(elements, pivot+1, high)
    

elements = [int(x) for x in input().split(" ")]
quick_sort(elements, 0, len(elements)-1)

print(elements)