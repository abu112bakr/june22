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

i=4
k=2
print("before while ", i ,"<",(len(source)-1))
while(i<len(source)-k):
    print("inside while ", i ,"<",(len(source)-1))
    i=i+1