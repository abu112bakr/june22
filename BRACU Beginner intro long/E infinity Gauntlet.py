#E infinity Gauntlet
#You took a peek on Thanos wearing Infinity Gauntlet. In the Gauntlet there is a place for six Infinity Gems:

#the Power Gem of purple color,
#the Time Gem of green color,
#the Space Gem of blue color,
#the Soul Gem of orange color,
#the Reality Gem of red color,
#the Mind Gem of yellow color.
#Using colors of Gems you saw in the Gauntlet determine the names of absent Gems.

#input
#In the first line of input there is one integer nn (0 \le n \le 60≤n≤6) — the number of Gems in Infinity Gauntlet.

#In next nn lines there are colors of Gems you saw. Words used for colors are: purple, green, blue, orange, red, yellow. It is guaranteed that all the colors are distinct. All colors are given in lowercase English letters.

#output
#In the first line output one integer mm (0 \le m \le 60≤m≤6) — the number of absent Gems.

#Then in mm lines print the names of absent Gems, each on its own line. Words used for names are: Power, Time, Space, Soul, Reality, Mind. Names can be printed in any order. Keep the first letter uppercase, others lowercase.


#sample 1
#input
#4
#red
#purple
#yellow
#orange
#output
#2
#Space
#Time

#sample 2
#Input
#0
#output
#6
#Time
#Mind
#Soul
#Power
#Reality
#Space
#Note
#In the first sample Thanos already has Reality, Power, Mind and Soul Gems, so he needs two more: Time and Space.
#In the second sample Thanos doesn't have any Gems, so he needs all six.

n=int(input())   #o to 6
#ourple,green,blue,orange,red,yellow
    #    0         1       2       3      4         5     
#list1=["purple","green","blue","orange","red","yellow"]
#list2=["Power","Time","Space","Soul","Reality","Mind"]
list1=["green","yellow","orange","purple","red","blue"]
list2=["Time","Mind","Soul","Power","Reality","Space"]
inputlist=[]
for i in range(0,n):
  x=input()
  inputlist.append(x)
print(6-n)
#print("inputlist",inputlist)
#print("list1",list1)
#print("list1",list1[4])
if len(inputlist)==0:
  for i in list2:
    print(i)
else:
  #
  for i in range(0,len(list1)):
    #
    # #print("i is",i)
    #if inputlist[i] in list1:
    if list1[i] in inputlist:
      pass
    else:
      print(list2[i])



#print(6-n)