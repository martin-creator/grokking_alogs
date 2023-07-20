# Divide and Conquer Algorithm
# This algorithm works by dividing the problem into smaller pieces, solving the smaller pieces, and then using that solution to solve the original problem.

# Example one sum of a list

def sum(list):
    if list == []: # base case
        return 0
    print(list)
    return list[0] + sum(list[1:]) # resursive case

print("sum of list")
print(sum([1, 2, 3, 4, 5]))


# Example two count the number of items in a list

def count(list):
    if list == []:
        return 0
    print(list)
    return 1 + count(list[1:])

print("count the number of items in a list")
print(count([1, 2, 3, 4, 5]))


# Example three find the max number in a list

def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    else:
        sub_max = max(list[1:])
        return list[0] if list[0] > sub_max else sub_max

print("Max number in list ")
print(max([1, 2, 3, 4, 5]))


# Example four binary search

def binary_search(list, item):
    if len(list) == 1: # base case
        return list[0] if list[0] == item else None
    else: # recursive case
        mid = int(len(list) / 2)
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            return binary_search(list[:mid], item)
        else:
            return binary_search(list[mid:], item)

print("Binary search")
print(binary_search([1, 2, 3, 4, 5], 3))