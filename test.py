#G - Ordinary Number
#problem statement
#we have a permutation {p1,p2,...,pn} of {1,2,....,n}
#print the number of elements pi(1<i<n) that satisfy the following condition:
#Pi is the second smallest number among the three numbers Pi-1,Pi,Pi+1
#
#constraints
#*All the values in the input are integers
#* 3<=n<=20
#*p is a permutation of {1,2,...,n}
#Input
#n
#P1,P2 ... Pn
#output
#print the number of elements Pi(1<i<n) that satisfy the condition

#sample 1
#input
#5
#1 3 5 4 2
#Output
#2
#P2=3 is the second smallest number among P1=1,P2=3, and P3=5. 
#Also, P4=4 is the second smallest number among P3=5, P4=4, and P5=2. 
#These two elements satisfy the condition.

#sample 2
#input
#9
#9 6 3 2 5 8 7 4 1
#output
#5

list=[1, 3, 5, 4, 2]
output=[]
for i in range(0,len(list)):
  pi_minus_1=i-1
  pi=i
  pi_plus_1=i+1
  if (pi_minus_1 and pi and pi_plus_1>-1) and (pi_minus_1 and pi and pi_plus_1<(len(list))) :
    smallest=list[pi]
    second_smallest=list[pi]
    if list[pi_minus_1]<smallest:
      second_smallest=smallest
      smallest=list[pi_minus_1]
    elif list[pi]<smallest:
      second_smallest=smallest
      smallest=list[pi]
    elif list[pi_plus_1]<smallest:
      second_smallest=smallest
      smallest=list[pi_plus_1]
    output.append(output)      
print(output)





