from random import randint,seed
import time
def merge(arr1,arr2):

    idx1 = 0 # keeping track of first arrays index
    idx2 = 0 # keeping track of second arrays index
    result = [None] * (len(arr1) + len(arr2))
    idxResult = 0

    while idx1 < len(arr1) and idx2<len(arr2): # untill one of the indexes end
        if arr1[idx1] < arr2[idx2]:
            result[idxResult] = arr1[idx1]
            idx1 = idx1 + 1
        else:
            result[idxResult] = arr2[idx2]
            idx2 = idx2 + 1
        idxResult = idxResult + 1

    while idx1 < len(arr1): # copy the rest over to result
        result[idxResult] = arr1[idx1]
        idxResult = idxResult + 1
        idx1 = idx1 + 1
    
    while idx2 < len(arr2): # copy the rest over to result
        result[idxResult] = arr2[idx2]
        idxResult = idxResult + 1
        idx2 = idx2 + 1
    
    return result

def mergeSort(arr,start,end):
    if (start == end) and (len(arr[start:end+1]) != 0): # if array has one element
        return [arr[start]]

    elif (start == end) and (len(arr[start:end+1]) == 0): # if array has no element
        return []
    
    
    halfPoint = int((end-start) / 2) # partition the array
    return merge(mergeSort(arr,start,start+halfPoint),mergeSort(arr,start+halfPoint + 1,end)) # merge two sub arrays




"""
*******************
FOR TESTING PURPOSES


seed(time.time())
arr = []
for _ in range(17):
    random = randint(0,2**10+1)
    arr.append(random)

print(mergeSort(arr,0,len(arr)))

*******************
"""
    


    


        


