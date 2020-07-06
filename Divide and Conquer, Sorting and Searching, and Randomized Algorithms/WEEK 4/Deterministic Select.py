import random
import time

random.seed(time.time())


def findIndexOfPivot(arr,start,end,pivot):
    for i in range(start,end):
        if arr[i] == pivot:
            return i
    #print("NO PIVOT FOUND!!!!!"+ " for " + str(pivot))

def chosePivot(arr,start,end):
    if start == end:
        return arr[start]
    if start > end:
        return
    
    n = end - start + 1
    if n <= 5:
        medianIndex = int(n / 2) if n % 2 == 0 else int((n + 1) / 2)
        return arr[start + medianIndex - 1]
    willAdd = False if end % 5 == 0 else True
    #groups = [sorted(arr[i:i+5] for i in range(start,end,5))]
    groups = []
    
    for i in range(start,end,5):
        dummy = arr[i:i+5].copy()
        dummy.sort()
        groups.append(dummy)

    if willAdd == False:
        pos = start
        while pos < end:
            pos = pos + 5
        dummy = arr[pos - n % 5 + 1:end+ n % 5].copy()
        dummy.sort()
        groups.append(dummy)
    medianGroup = []
    for group in groups:
        ngroup = len(group)
        if ngroup != 0:
            medianIndex = int(ngroup / 2) if ngroup % 2 == 0 else int((ngroup + 1) / 2)
            medianGroup.append(group[medianIndex - 1])
    return chosePivot(medianGroup,0,len(medianGroup) - 1)


def partition(arr,start,end):
    p = arr[start] # chose the pivot as first element for now
    i = start + 1 # i denotes the left most index s.t arr[i]>p
    for j in range(start+1,end+1):
        if arr[j] < p: # if element seen is smaller
            arr[i],arr[j] = arr[j],arr[i] # swap with left most element >p
            i = i+1 # advance the boundry
    arr[i-1],arr[start] = arr[start],arr[i-1] # put the pivot into place
    return i-1 # position of pivot


def deterministicSelect(arr,start,end,i):
    if start == end:
        return arr[start]
    if start > end:
        return

    pivot = findIndexOfPivot(arr,start,end,chosePivot(arr,start,end))
    arr[start],arr[pivot] = arr[pivot],arr[start] # swap the pivot with first element for partition subroutine
    positionOfPivot = partition(arr,start,end)

    j = positionOfPivot - start + 1 # order statistic wrt to starting index

    if i == j:
        return arr[positionOfPivot]
    elif i > j:
        return deterministicSelect(arr,positionOfPivot+1,end,i - j) # look for the order statistic at right
    else:
        return deterministicSelect(arr,start,positionOfPivot-1,i) # look for the order statistic at left



"""
TEST CODE, GIVES ERROR FOR SOME CASES BUT I DID NOT FIGURE OUT
IT PRODUCES A PIVOT THAT IS NOT IN THE ORIGINAL ARRAY
n = random.randint(1,200)
i = random.randint(1,n)

arr = [random.randint(-100,300) for _ in range(n)]
num = deterministicSelect(arr,0,len(arr)-1,i)

arr.sort()
assert arr[i-1] == num
"""

