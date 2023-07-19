# Stack 
# This is a data structure that consists of Nodes. Each Node references the next Node in the stack, but does not reference its previous.
# Real world example: a stack of plates, or a stack of books, or a stack of anything.
# The basic operations of a stack are: Push, Pop, and Peek.
# Push: add a Node to the top of the stack
# Pop: remove a Node from the top of the stack
# Peek: see the value of the top Node in the stack
# Examples of stacks in apps include : managing function invocations, undo/redo, routing (the history object), and much more!

# # Example 1 factorial using a stack

def factorial(num):
    # establish base case
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1) # Recursive case

print(factorial(5))

# visualie the factorial function using a stack
# factorial(5)
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1 * factorial(0)
# 5 * 4 * 3 * 2 * 1 * 1
# 5 * 4 * 3 * 2 * 1
# 5 * 4 * 3 * 2
# 5 * 4 * 6
# 5 * 24
# 120

# Example 2: Convert an integer to a string in any base

def toStr(num, base):
    convertString = "0123456789ABCDEF"
    # establish base case
    if num < base:
        return convertString[num]
    else:
        return toStr(num // base, base) + convertString[num % base] # Recursive case

print(toStr(1453, 16))
