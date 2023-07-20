# Quick sort
# The quick sort algorithm is a divide and conquer algorithm. It picks an element as a pivot and partitions the given array around the picked pivot. There are many different versions of quick sort that pick pivot in different ways.
# The different versions of quick sort choose the pivot in different like the first element, the last element, the median, or a random element. The worst case run time of quick sort is O(n^2) but the average case is O(nlogn). The space complexity is O(logn).


# Example of quick sort

def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        # sub-array of all the elements less than the pivot
        less = [i for i in array[1:] if i <= pivot]
        # sub-array of all the elements greater than the pivot
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


print ("Quick sort")
# add an array of 20 random numbers
print(quick_sort([10, 5, 2, 3, 4, 7, 9, 8, 6, 1, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))


# Example of quick sort with a random pivot

import random

def quick_sort_random(array):
    if len(array) < 2:
        return array
    else:
        pivot = random.choice(array)
        # sub-array of all the elements less than the pivot
        less = [i for i in array[1:] if i <= pivot]
        # sub-array of all the elements greater than the pivot
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort_random(less) + [pivot] + quick_sort_random(greater)


print ("Quick sort with random pivot")
# add an array of 20 random numbers
print(quick_sort_random([10, 5, 2, 3, 4, 7, 9, 8, 6, 1, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))


# Example of quick sort with a median pivot

def quick_sort_median(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[len(array) // 2]
        # sub-array of all the elements less than the pivot
        less = [i for i in array[1:] if i <= pivot]
        # sub-array of all the elements greater than the pivot
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort_median(less) + [pivot] + quick_sort_median(greater)


print ("Quick sort with median pivot")
# add an array of 20 random numbers
print(quick_sort_median([10, 5, 2, 3, 4, 7, 9, 8, 6, 1, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))


# Which pivot is best?
# The median pivot is the best pivot because it will always divide the array into two equal parts. The random pivot is the second best pivot because it will divide the array into two parts that are not equal but are close to equal. The first element pivot is the worst pivot because it will divide the array into two parts that are not equal and are not close to equal. The worst case run time of quick sort is O(n^2) but the average case is O(nlogn). The space complexity is O(logn).



# Implementing a quick sort algo

def quick_sort_test(arr):

    if len(arr) < 2:
        return arr
    else:
        pivot = arr[len(arr) //2]
        lesser = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]

        return quick_sort_test(lesser) + [pivot] + quick_sort_test(greater)


print ("Quick sort test")
# add an array of 20 random numbers
print(quick_sort_test([10, 5, 2, 3, 4, 7, 9, 8, 6, 1, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))


