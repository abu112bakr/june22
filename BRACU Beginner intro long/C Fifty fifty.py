#C _Fifty-Fifty

#problem statement
#You are given a 44-character string SS consisting of uppercase English letters. Determine if SS consists of exactly two kinds of characters which both appear twice in SS.
#constraints
#The length of SS is 44.
#SS consists of uppercase English letters.
#Input
#S
#input

#output
#If SS consists of exactly two kinds of characters which both appear twice in SS, print Yes; otherwise, print No.

#Sample 1 input , output
#ASSA
#Yes
#Sample 2 input , output
#STOP
#No
#Sample 3 input , output
#FFEE
#Yes
#Sample 4 input , output
#FREE
#No


S=input()
a=S[0]
b=S[1]
condition=True
for i in S:
  if S.count(i)!=2:
    condition = False
if condition==True:
  print("Yes")
elif condition==False:
  print("No")
#ASSA	Yes
#STOP	No
#FFEE	Yes
#FREE	No

