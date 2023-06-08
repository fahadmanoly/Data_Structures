lis=[3,6,1,7,9,3,2,5,4,8]
print(lis)
for i in range(len(lis)-1):
    max_ind=i
    for j in range(i+1,len(lis)):
        if lis[j] > lis[max_ind]:
            max_ind = j
    if lis[i] != lis[max_ind]:
        lis[i],lis[max_ind] = lis[max_ind],lis[i]
print(lis)
