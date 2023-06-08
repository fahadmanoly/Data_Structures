lis=[3,6,1,7,9,3,2,5,4,8]
print(lis)
for i in range(len(lis)-1):
    swapped=False
    for j in range(len(lis)-1-i):
        if lis[j] > lis[j+1]:
            lis[j],lis[j+1] = lis[j+1],lis[j]
            swapped=True
    if not swapped:
        print('n order')
        break
print(lis)