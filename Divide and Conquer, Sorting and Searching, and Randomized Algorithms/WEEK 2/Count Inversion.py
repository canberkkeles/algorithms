with open("IntegerArray.txt","r") as f:
    arr = [int(integers.rstrip()) for integers in f.readlines()]


def mergeForInversion(arr1,arr2):
    idx1 = 0 # keeping track of first arrays index
    idx2 = 0 # keeping track of second arrays index
    result = [None] * (len(arr1) + len(arr2))
    idxResult = 0
    inversionCount = 0 # newly added inversionCount

    while idx1 < len(arr1) and idx2<len(arr2): # untill one of the indexes end
        if arr1[idx1] < arr2[idx2]:
            result[idxResult] = arr1[idx1]
            idx1 = idx1 + 1
        else:
            result[idxResult] = arr2[idx2]
            inversionCount = inversionCount + (len(arr1) - idx1) # if second half number is bigger, increase inversionCount
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

    return result,inversionCount


def countInversion(arr,start,end):

    inversionCount = 0
    if (start == end) and (len(arr[start:end+1]) != 0): # if array has one element
        return [arr[start]],inversionCount

    elif (start == end) and (len(arr[start:end+1]) == 0): # if array has no element
        return [],inversionCount

    halfPoint = int((end-start) / 2)

    firstHalf, firstHalfInversions = countInversion(arr,start,start+halfPoint) # firstHalf sorted and inversionCount
    secondHalf, secondHalfInversions = countInversion(arr,start+halfPoint+1,end) # secondHalf sorted and inversionCount

    splitResult,splitInversions = mergeForInversion(firstHalf,secondHalf) # splitResult sorted and inversionCount
    inversionCount = inversionCount + firstHalfInversions + secondHalfInversions + splitInversions
    return splitResult, inversionCount






"""
FOR TESTING PURPOSES
res,inv = countInversion(arr,0,len(arr))
print(inv)
"""

