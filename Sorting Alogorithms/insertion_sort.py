def insertionsort(arr):
    for i in range(1,len(arr)):
        current_element=arr[i]
        pos=i
        while current_element < arr[pos-1] and pos>0:
            arr[pos]=arr[pos-1]
            pos=pos-1
        arr[pos]=current_element

lis=[3,5,7,2,8,9,1]
insertionsort(lis)
print(lis)
