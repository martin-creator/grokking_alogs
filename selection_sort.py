# selction sort algo
# it has O(n^2)

testArr = [5, 3, 6, 2, 10, 100, 50, 4000, 5000 ]
binArr = [1, 2, 3, 4, 7, 9]

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


# Implement a binary search algorithm

def binary_search(list, item):
    # the list must be sorted
    # establish a low
    # establish a high
    low = 0
    high = len(list) - 1

    while low <= high:
        mid =  int((low + high ) / 2)
        guess = list[mid]

        if guess == item:
            return mid

        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None



print("------------------Selection Sort -------------------")
print(selectionSort(testArr))
print("------------------Binary Sort -------------------")
print(binary_search(binArr, 9))
