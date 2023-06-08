def finding_pivot(arr,first,last):
    pivot=arr[first]
    left=first+1
    right=last
    while True:
        while left<=right and arr[left] <= pivot:
            left=left+1
        while left<=right and arr[right] >= pivot:
            right=right-1
        if left > right:
            break
        else:
            arr[left],arr[right]=arr[right],arr[left]

    arr[first],arr[right]=arr[right],arr[first]
    return right

def quicksort(arr,first,last):
    if first<last:
        p=finding_pivot(arr,first,last)
        quicksort(arr,first,p-1)
        quicksort(arr,p+1,last)

lis=[3,1,7,45,78,12,88,44,27,43]
quicksort(lis,0,9)
print(lis)
