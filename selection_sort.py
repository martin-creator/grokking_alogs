# selction sort algo
# it has O(n^2)

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    
    return smallest_index



def selectionSort(arr):
    sortedArr =  []

    for i in range(len(arr)):
        smallest = findSmallest(arr)
        sortedArr.append(arr.pop(smallest))

    return sortedArr

print(selectionSort([5, 3, 6, 2, 10, 100, 50, 4000, 5000 ]))