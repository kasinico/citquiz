#1. Using a while loop, implement bubble sort algorithm 
#2. Using a while loop, implement selection sort algorithm 
""""
def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        curr_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[curr_idx]:
                curr_idx = j

        #our swapping  (i,curr_idx)
        arr[i], arr[curr_idx] = arr[curr_idx],arr[i] 
arr = [2, 6, 5, 1, 3, 4]
selection_sort(arr)
print(arr)
"""

#
def selection_sort(arr):
    # [2, 6, 5, 1, 3, 4]
     i = 0
     curr_idx = len(arr)
     while (i<curr_idx):
        j = i+1
        while (j<curr_idx):
           if arr[i] > arr[j]: #we check if i > j
               arr[i], arr[j] = arr[j], arr[i]
           j+=1
        i+=1
     #print(f" {arr}")
      # [2, 6, 5, 1, 3, 4]
arr = [2, 6, 5, 1, 3, 4]
selection_sort(arr)
print(arr)