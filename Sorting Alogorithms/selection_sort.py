lis=[3,6,1,7,9,3,2,5,4,8]
print(lis)
for i in range(len(lis)):
    min_ind=i
    for j in range(i+1,len(lis)):
        if lis[j]<lis[min_ind]:
            min_ind=j
    
    if lis[i]!=lis[min_ind]:
        lis[i],lis[min_ind]=lis[min_ind],lis[i]
        
print(lis)

