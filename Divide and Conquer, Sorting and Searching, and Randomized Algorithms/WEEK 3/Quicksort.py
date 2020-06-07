

comparisonCount = 0

with open("QuickSort.txt","r") as f:
    arr = [int(integers.rstrip()) for integers in f.readlines()]

def medianOfThree(start,end):
    length = end - start + 1
    middleIndex = int(length/2) - 1 if length % 2 == 0 else int(length/2)
    middleIndex = start + middleIndex # move middleIndex to correct position

    firstElement = arr[start]
    lastElement = arr[end]
    middleElement = arr[middleIndex]

    if firstElement <= middleElement <= lastElement or lastElement <= middleElement <= firstElement:
        return middleIndex
    elif middleElement <= firstElement <= lastElement or lastElement <= firstElement <= middleElement:
        return start
    elif middleElement <= lastElement <= firstElement  or  firstElement <= lastElement <= middleElement:
        return end
    


def partition(arr,start,end):
    global comparisonCount
    comparisonCount = comparisonCount + (end-start)
    p = arr[start] # chose the pivot as first element for now
    i = start + 1 # i denotes the left most index s.t arr[i]>p
    for j in range(start+1,end+1):
        if arr[j] < p: # if element seen is smaller
            arr[i],arr[j] = arr[j],arr[i] # swap with left most element >p
            i = i+1 # advance the boundry
    arr[i-1],arr[start] = arr[start],arr[i-1] # put the pivot into place
    return i-1 # position of pivot


def quicksort(arr,start,end):
    if start >= end:
        return

    pivot = start # index for pivot element, modify this for assignment
    arr[start],arr[pivot] = arr[pivot],arr[start] # swap the pivot with first element for partition subroutine
    positionOfPivot = partition(arr,start,end)


    quicksort(arr,start,positionOfPivot-1)
    quicksort(arr,positionOfPivot+1,end)

    return

quicksort(arr,0,len(arr)-1)
print(arr)
print(comparisonCount)

