A=[5,1,9,-3]
for i in range(1,len(A)):
    t=A[i]
    j=i-1
    while(j==0 and A[j]>t):
        A[j+1]=A[j]
        j=j-1
    A[j+1]=t
print(A)




