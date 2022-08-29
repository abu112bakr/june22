#Task 3                                                               NOT DONE
#Sort a singly linked sequential list using bubble sort algorithm.
class Node:
  def __init__(self, e, n):
    self.element = e
    self.next = n
#A=[1,2,3,4]
#head=Node(A[0],None)
#tail=head
##make linked list recursiely not using loop
#for i in range(1,len(A)):
#  temp_node=Node(A[i],None)
#  tail.next=temp_node
#  tail=tail.next

head=Node(64,None)
b=Node(25,None)
c=Node(12,None)
d=Node(22,None)
e=Node(11,None)
head.next=b
b.next=c 
c.next=d
d.next=e
print(head.element,b.element,c.element,d.element,e.element)
print()
def getNode(head,i):
    #
  
    if i==0:
        #
        return head
    else:
        #
        c=0
        x=head
    while c!=i:
        #
        c+=1
        x=x.next
    return x
#normally
A=[65,25,12,22,11]
def bubblesort_normally(A):
  for i in range(0,len(A)):
    for j in range(i+1,len(A)):
      if A[j]<A[i]:
        t=A[i]
        A[i]=A[j]
        A[j]=A[i]
        #done xD
  return A
def bubblesort_recursive(head,i,length):
    
    #
  
    for j in range(i+1,length):
        #
        print(j,end=" ")
    #
        if getNode(head,j).element<getNode(head,i).element:
            #
        #
            t=getNode(head,i).element
            getNode(head,i).element=getNode(head,j).element
            getNode(head,j).element=t
    i+=1
    if i<length:

        bubblesort_recursive(head,i,length)

bubblesort_recursive(head,0, 5)

print(getNode(head,0).element)
print(getNode(head,1).element)
print(getNode(head,2).element)
print(getNode(head,3).element)
print(getNode(head,4).element)
