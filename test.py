#left shift like lab sir
#Na parle chobi akba works
def shift_left(source, k):
  i=0
  while(i<len(source)-k):
    print("inside while ", i ,"<",(len(source)-1))
    source[i]=source[i+k]
    i=i+1
  
  j=len(source)-1 #5
  count=0
  while(count<k):
    #print("I am here")
    
    #source[j]=0
    j=j-1
    count+=1
source=[10,20,30,40,50,60]
#print(source,"   1")
shift_left(source,1)
#print(source)

print()
source=[10,20,30,40,50,60]
print(source,"   2")
shift_left(source,2)
print(source)

print()
source=[10,20,30,40,50,60]
#print(source,"   3")
#shift_left(source,3)
#print(source)

print()
source=[10,20,30,40,50,60]
#print(source,"   4")
#shift_left(source,4)
#print(source)