# Recursion
# This is when a function calls itself

# Example 1 Psuedo code

# def look_for_key(main_box):
#     pile = main_box.make_a_pile_to_look_through()

#     while pile is not empty:
#         box = pile.grab_a_box()
#         for item in box:
#             if item.is_a_box():
#                 pile.append(item)
#             elif item.is_a_key():
#                 print("found the key!")


# # Example 2 Psuedo code

# def look_for_key(box):
#     for item in box:
#         if item.is_a_box(): # Recursive Case
#             look_for_key(item) # <--- Recursion
#         elif item.is_a_key(): # Base Case
#             print("found the key!")


# # Example 3 Count down to zero

def count_down(num):
    # establish base case:
    if num == 0:
        print("Done!")
        return
    else:
        print(num)
        count_down(num - 1)

# print(count_down(100))

# Example 4 Sum of a list

def sum(arr):
    # establish base case
    if arr == []:
        return 0
    else:
        return arr[0] + sum(arr[1:]) # Recursive case

# print(sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# Example 5 Count number of items in a list

def count(arr):
    # establish base case
    if arr == []:
        return 0
    else:
        return 1 + count(arr[1:]) # Recursive case

# we begin adding from one because we are counting the first item in the list

print(count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# Example 6 Find the max number in a list

def max(arr):
    # establish base case
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    else:
        sub_max = max(arr[1:]) # sub_max is the max of the sub array
        return arr[0] if arr[0] > sub_max else sub_max

print (max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))



# Visualizing Recursion

# max([4, 8, 2, 10, 6])
# |
# |--> max([8, 2, 10, 6])
# |    |
# |    |--> max([2, 10, 6])
# |    |    |
# |    |    |--> max([10, 6])
# |    |    |    |
# |    |    |    |--> max([6]) -> returns 6 (base case)
# |    |    |
# |    |    |--> Returns max(10, 6) -> returns 10
# |    |
# |    |--> Returns max(8, 10) -> returns 10
# |
# |--> Returns max(4, 10) -> returns 10






