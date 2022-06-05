def right_shift(A):
    i=len(A)-1
    #i=0
    while(i>0):
        A[i]=A[i-1]
        i=i-1
    A[0]=0

A=[1,2,3,4,5]
print(A)
right_shift(A)
print(A)
right_shift(A)
print(A)
right_shift(A)
print(A)
right_shift(A)
print(A)
right_shift(A)
print(A)
right_shift(A)
print(A)