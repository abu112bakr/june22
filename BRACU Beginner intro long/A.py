#A
#input
#2
#1 7
#9 8
#output
#Case 1: 8
#Case 2: 17

T=int(input())
case=1
for i in range(T):
    string=input()
    a,b=string.split(" ")
    a=int(a)
    b=int(b)
    temp=a+b
    #print("Case 1: 8")
    case_temp=str(case)
    temp_temp=str(temp)
    print("Case "+case_temp+": "+temp_temp)
    case+=1

