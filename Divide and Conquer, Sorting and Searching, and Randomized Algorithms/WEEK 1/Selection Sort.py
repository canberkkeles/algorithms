from random import randint,seed
import time
def selectionSort(arr):
    for i in range(len(arr) - 1): # suppose the beginning of the array is sorted, move beginning everytime
        minNumber = arr[i]
        minidx = i
        for j in range(i+1,len(arr)): # find min in remaining array
            if arr[j] < minNumber:
                minidx = j
                minNumber = arr[j]
        arr[i],arr[minidx] = arr[minidx],arr[i] # swap min
    return arr


"""
********************
FOR TESTING PURPOSES

seed(time.time())
arr = []
for _ in range(30):
    random = randint(0,2**10+1)
    arr.append(random)

print(selectionSort(arr))


"""
    

