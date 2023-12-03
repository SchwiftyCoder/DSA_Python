# start with the array with the largest size
def mergeSortedArrays(arr1, arr2):
    mergedArray = []
    # best case scenario: one array is empty
    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1
    
    # pointers to step through array by index
    pointer1 = 0
    pointer2 = 0 

    #
    while(pointer1 < len(arr1) and  pointer2 < len(arr2)):   
        if arr1[pointer1] < arr2[pointer2]:
            mergedArray.append(arr1[pointer1]) 
            pointer1 += 1
        elif arr2[pointer2] < arr1[pointer1]:
            mergedArray.append(arr2[pointer2]) 
            pointer2 += 1
        else: 
            mergedArray.append(arr1[pointer1])
            mergedArray.append(arr2[pointer2])
            pointer1 += 1
            pointer2 += 1

    # append any remaining element to the end of the merged array 
    mergedArray.extend(arr1[pointer1:])
    mergedArray.extend(arr2[pointer2:])
    
    return mergedArray

print(mergeSortedArrays([0, 3, 4, 6, 31], [-90, -34, -1, 0, 4, 6, 30]))
