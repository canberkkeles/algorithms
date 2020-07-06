import random
import time

random.seed(time.time())

def partition(arr,start,end):
    p = arr[start] # chose the pivot as first element for now
    i = start + 1 # i denotes the left most index s.t arr[i]>p
    for j in range(start+1,end+1):
        if arr[j] < p: # if element seen is smaller
            arr[i],arr[j] = arr[j],arr[i] # swap with left most element >p
            i = i+1 # advance the boundry
    arr[i-1],arr[start] = arr[start],arr[i-1] # put the pivot into place
    return i-1 # position of pivot


def randomizedSelect(arr,start,end,i):
    if start == end:
        return arr[start]
    if start > end:
        return

    pivot = random.randint(start,end)
    arr[start],arr[pivot] = arr[pivot],arr[start] # swap the pivot with first element for partition subroutine
    positionOfPivot = partition(arr,start,end)

    j = positionOfPivot - start + 1 # order statistic wrt to starting index

    if i == j:
        return arr[positionOfPivot]
    elif i > j:
        return randomizedSelect(arr,positionOfPivot+1,end,i - j) # look for the order statistic at right
    else:
        return randomizedSelect(arr,start,positionOfPivot-1,i) # look for the order statistic at left


"""
TEST CODE
n = random.randint(0,100)
i = random.randint(1,n)

arr = [random.randint(-100,300) for _ in range(n)]
num = randomizedSelect(arr,0,len(arr)-1,i)

arr.sort()

assert arr[i-1] == num
"""