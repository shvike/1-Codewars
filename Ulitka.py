from pprint import pprint

m = 9
n = 6

arr = []
counter = 0
for i in range(n):
    arr.append([])
    for j in range(m):
        counter += 1
        arr[i].append(counter)
        # arr[i] += str(counter) + '\t'


max_element_digits = len(str(m*n))
arr2 = arr.copy()
for i in range(n):
    for j in range(m):
        arr2[i][j] = str(arr[i][j]).center(max_element_digits)

pprint(arr2)