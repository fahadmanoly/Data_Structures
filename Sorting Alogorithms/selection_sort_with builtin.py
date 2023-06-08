lis=[3,6,1,7,9,3,2,5,4,8]
print(lis)

for i in range(len(lis)-1):
    min_val=min(lis[i:])
    min_ind=lis.index(min_val,i)
    lis[i],lis[min_ind]=lis[min_ind],lis[i]
print(lis)

