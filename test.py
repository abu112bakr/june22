def right_shift(A):
    j=0
    x=int(input("digit "))
    while (j<x):
        i=len(A)-1
        
        while(i>0):
            A[i]=A[i-1]
            i=i-1
        A[0]=0
        j=j+1
A=[1,2,3,4,5]
print(A)
right_shift(A)
print(A)



##tewst




