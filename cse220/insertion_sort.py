#insertion sort bux code
A=[5,1,9,-3]
#  j i
for i in range(1,len(A)):
    key=A[i]
    j=i-1
    while(j>=0 and key<A[j]):
        A[j+1]=A[j]
        j=j-1
    A[j+1]=key

print(A)




