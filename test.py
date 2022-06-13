#4
#Rotate Right k cells 
# Consider an array named source. Write a method/function named rotateRight( source, k) 
#that rotates all the elements of the source array to the right by 'k' positions. 
#You must execute the method by passing an array and number of cells to be shifted. 
#After calling the method, print the array to show whether the elements have been shifted properly.
#Example:
#source=[10,20,30,40,50,60]
#rotateRight(source,3)
#After calling rotateRight(source,3), printing the array should give the output as: 
# [ 40, 50, 60, 10, 20, 30]

#Rak sir method
def rotateRight( source, k):

  j=0
  while(j<k):
    i=len(source)-1
    temp=source[i]  #new last index is stored
    while (i>=1):
      source[i]=source[i-1]
      i=i-1
    source[0]=temp  #new first index = saved index
    j=j+1
source=[10,20,30,40,50,60]
print(source)
rotateRight(source,3)
print(source)
print("##########################")
#DOME BY SIR HIMSELF
##rotate right LAB-sir     #have to work dynamcally
def rotate_Right(source,k):  #see phone pic
  temp_array=[0]*k
  t = k-1
  for i in range(len(source)-1,len(source)-1-k,-1):
    temp_array[t]=source[i]
    t -= 1
  #print(temp_array)
  i=len(source)-1
  while(i>=k):
    source[i]=source[i-k]   #new
    i=i-1
#  j=0
#  while(j<k):
#    source[j]=0
#    j=j+1
  j=0
  while(j<k):
    source[j]=temp_array[j]
    j=j+1
source=[10,20,30,40,50,60]
print(source)
rotate_Right(source,3)
print(source)
#Done :)