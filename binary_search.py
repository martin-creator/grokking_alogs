# Binary Search Algorithms
# It reduces the search time by half, 2* = number of items
# It is always log to base 2
# The provided list should always be sorted
# * is the number of steps it will take the binary search algo
# Big O notation lets you compare the number of operations. It tells you how fast the algorithm grows.

def binary_search(list, item):
    # set boundaries
    low = 0 
    high = len(list) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = list[mid]

        if guess == item:
            return mid
        
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None

my_list = [1, 2, 3, 4, 7, 9]

print(binary_search(my_list, 4))

# Binary search is O(logn)
# The travelling sales man problem has run time of O(n!)


# Visualize binary search
# my_list = [1, 2, 3, 4, 7, 9]
# binary_search(my_list, 3)
# | low = 0, high = 5, mid = 2, guess = 3
# | low = 0, high = 1, mid = 0, guess = 1
# | low = 1, high = 1, mid = 1, guess = 2
# | low = 2, high = 1, mid = 2, guess = 3
# | low = 2, high = 1, mid = 2, guess = 3