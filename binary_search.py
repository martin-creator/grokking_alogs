# Binary Search Algorithms
# It reduces the search time by half, 2* = number of items
# It is always log to base 2
# The provided list should always be sorted
# * is the number of steps it will take the binary search algo

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = int((high + low) / 2)
        guess = list[mid]

        if guess == item:
            return mid
        
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None

my_list = [1, 2, 3, 4, 7, 9]

print(binary_search(my_list, 5))