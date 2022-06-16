#F - Greg`s Workout
#https://vjudge.net/contest/499284#problem/F
#Greg is a beginner bodybuilder. Today the gym coach gave him the training plan. All it had was n integers a1, a2, ..., an. These numbers mean that Greg needs to do exactly n exercises today. Besides, Greg should repeat the i-th in order exercise ai times.
#Greg now only does three types of exercises: "chest" exercises, "biceps" exercises and "back" exercises. Besides, his training is cyclic, that is, the first exercise he does is a "chest" one, the second one is "biceps", the third one is "back", the fourth one is "chest", the fifth one is "biceps", and so on to the n-th exercise.
#Now Greg wonders, which muscle will get the most exercise during his training. We know that the exercise Greg repeats the maximum number of times, trains the corresponding muscle the most. Help Greg, determine which muscle will get the most training.

#input
#The first line contains integer n (1 ≤ n ≤ 20). The second line contains n integers a1, a2, ..., an (1 ≤ ai ≤ 25) — the number of times Greg repeats the exercises.
#output
#Print word "chest" (without the quotes), if the chest gets the most exercise, "biceps" (without the quotes), if the biceps gets the most exercise and print "back" (without the quotes) if the back gets the most exercise.
#It is guaranteed that the input is such that the answer to the problem is unambiguous.

#sample 1
#input
#2
#2 8
#output
#biceps

#sample 2
#input
#3
#5 1 10
#output
#back

#sample 3
#input
#7
#3 3 2 7 9 6 8
#output
#chest

#note
#In the first sample Greg does 2 chest, 8 biceps and zero back exercises, so the biceps gets the most exercises.
#In the second sample Greg does 5 chest, 1 biceps and 10 back exercises, so the back gets the most exercises.
#In the third sample Greg does 18 chest, 12 biceps and 8 back exercises, so the chest gets the most exercise.
from asyncio.windows_events import NULL
from textwrap import indent


input_list=[]
n=int(input())
string=input()
string=string.split(" ")
for item in string:
  input_list.append(int(item))
#input_list=[3,3,2 , 7,9,6 , 8]
#           0 1 2   3 4 5   6
#input_list=[1,2,3 , 1,2,3 , 1]


outputlist=[0,0,0]
for i in range(0,len(input_list),3):  #frint fist 
  #i jumps to the first digit of 3 block
  x=i
  count=0
  for j in range(x,x+3):
    if j>(len(input_list)-1):
      break
    #print(input_list[j],end=" ")
    temp=outputlist[count]+input_list[j]
    outputlist[count]=temp
    count=count+1
    if count>2:
      count=0

  #print(input_list[i])
  #print()
#print()
#for i in range(0,len(input_list),2):  #frint fist 
#  print(input_list[i])
#print(outputlist)
def return_max_index(list):
  max=list[0]
  index=NULL
  for i in range(0,len(list)):
    if list[i]>max:
      index=i
      max=list[i]
  return index

x=return_max_index(outputlist)
if x==0:
  print("chest")
elif x==1:
  print("biceps")
elif x==2:
  print("back")





