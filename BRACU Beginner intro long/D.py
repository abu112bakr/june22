#Capitalization is writing a word with its first letter as a capital letter. Your task is to capitalize the given word.
#Note, that during capitalization all the letters except the first one remains unchanged.
#A single line contains a non-empty word. This word consists of lowercase and uppercase English letters. The length of the word will not exceed 103.
#Output the given word after capitalization.


#ApPLe  outut ApPLe

#konjac output  Konjac



string=input()
#string="aPPLE"
#string="ball"
#string="ABC"
list=[]
for i in string:
  list.append(i)
#list=string.split()
#print(list)
first=int(ord(list[0]))
if first<123 and 96<first:
  
  first=first-32
  #print("i am here",first)
  list[0]=chr(first)
emptystring=""
for i in list:
  temp=str(i)
  emptystring=emptystring+temp
print(emptystring)