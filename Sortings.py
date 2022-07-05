a = [5, 3, 4, 8, 9, 2, 0, 1]

# def bubble_sort(a: list) -> list:
#     for i in range(len(a)):
#         swamp = False
#         for j in range(len(a) - i - 1):
#             if a[j] > a[j + 1]:
#                 a[j], a[j + 1] = a[j + 1], a[j]
#                 swamp = True
#         if swamp == False:
#             break
#     return a
#
# print(bubble_sort(a))



def selectionSort(data):
    for scanIndex in range(0, len(data)):
        minIndex = scanIndex
        for compIndex in range(scanIndex + 1, len(data)):
            if data[compIndex] < data[minIndex]:
                minIndex = compIndex
        if minIndex != scanIndex:
            data[scanIndex], data[minIndex] = data[minIndex], data[scanIndex]
    return data

result = selectionSort(a)
print(result)

