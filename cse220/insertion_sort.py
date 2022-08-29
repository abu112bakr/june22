#insertion sort bux code

#Input: 17 3 9 21 2 7 5
#n = 7
#Step 1: 17 | 3 9 21 2 7 5 << move 3 to the left
#Step 2: 3 17 | 9 21 2 7 5 << move 9 to the left

#Step 3: 3 9 17 | 21 2 7 5 << move 21 to the left
#Step 4: 3 9 17 21 | 2 7 5 << move 2 to the left
#Step 5: 2 3 9 17 21 | 7 5 << move 7 to the left
#Step 6: 2 3 7 9 17 21 | 5 << move 5 to the left
#: 2 3 5 7 9 17 21 5 | << STOP




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




