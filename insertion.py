#1. Using a while loop, implement bubble sort algorithm 
#2. Using a while loop, implement selection sort algorithm 
def insertion_sort(arr):
    for i in range(1, len(arr)):
        next_item = i
        while arr[next_item-1] > arr[next_item] and next_item > 0:
            arr[next_item - 1], arr[next_item] = arr[next_item], arr[next_item-1]
            next_item -= 1


arr = [-2, 45, 0, 11, -9]
insertion_sort(arr)
print('Sorted Array in Ascending Order:')
print(arr)