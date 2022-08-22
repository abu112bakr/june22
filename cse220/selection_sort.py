A=[5,1,9,-3]
for i in range(0,len(A)):
    minIndex=i  #new
    for j in range(i+1,len(A)):
        if(A[j]<A[i]):
            minIndex=j
    t=A[i]
    A[i]=A[minIndex]
    A[minIndex]=t
print(A)