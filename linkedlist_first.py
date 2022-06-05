#week 1 lecture sheet
#creating array
#iterating over the elements of an array
#copying an array
#resizing an array
#reversing an array
#shifing an array left          //sir method 5th june
#shiffing an array right          //sir method 5th june
#inserting an elemet into an arry          //sir method 5th june
#removing an elemt from an array          //sir method 5th june
#rotating an array left          //sir method 5th june
#rotating an array right          //sir method 5th june

#first of all list is not array
#u cannot expand arrray
#u cannot append array

#some basic things https://www.w3schools.com/python/python_arrays.asp

#creating an array with size array=[0]*5
from multiprocessing import Condition


myarray=[0]*5
myarray[0]=1
myarray[1]=2
myarray[2]=3
myarray[3]=4
myarray[4]=5
print(myarray)
#iterating over the elements of an array
#while loop
print("30")
i=0
while i<len(myarray):
    print(myarray[i])
    i=i+1
#for loop
print("35")
for i in range(0,len(myarray)):
    print(myarray[i])
#copying an array
print("40")
originalarray=myarray
def copyarray(oldarray):
    newarray=[0]*int(len(oldarray))
    for i in range(0,len(oldarray)):
        newarray[i]=oldarray[i]
        i=i+1
    return(newarray)
newar_array=copyarray(originalarray)
print(newar_array)
#resizing an array
print("51")
def resize(oldarray,resize_factor):
    if resize_factor>0:
        newarray=[0]*int(len(oldarray)+resize_factor)
        for i in range(0,len(oldarray)):
            newarray[i]=oldarray[i]
            i=i+1
        return(newarray)
    elif(resize_factor<0):#negative
        newarray=[0]*int(len(oldarray)+resize_factor)
        #print(str(len(oldarray))+str(resize_factor)+"="+str(int(len(oldarray)-resize_factor)))
        #                      ex 5+(-2)=3
        for i in range(0,int(len(oldarray)+resize_factor)):
            newarray[i]=oldarray[i]
            i=i+1
        return(newarray)
originalarray=copyarray(myarray)       #change here
newar_array=resize(originalarray,5)
print(newar_array)
newar_array=resize(originalarray,-2)
print(newar_array)
##reversing an array    #we reverse the itself array
print("73")
def reverse(oldarray):
    temparray=[0]*int(len(oldarray))
    j=0
    for i in range(int(len(oldarray)-1),-1,-1):
        #print(i)
        temparray[j]=oldarray[i]
        j=j+1
    for i in range(0,int(len(oldarray))):
        oldarray[i]=temparray[i]
    return oldarray
originalarray=copyarray(myarray)       #change here
originalarray=reverse(originalarray)
print(originalarray)
##shifing an array left
print("88")
def shift_left(oldarray,shift_factor):
    newarray=[0]*len(oldarray)
    j=0
    for i in range(shift_factor,len(oldarray)):
        newarray[j]=oldarray[i]
        j=j+1
    #print(newarray)
    return(newarray)
originalarray=copyarray(myarray)       #change here
newar_array=shift_left(originalarray,1)     #shift factor works exactly with 1 2 3 4 5 6 7... also 0
print(newar_array)
print("100")
def shift_right(oldarray,shift_factor):
    newarray=[0]*len(oldarray)
    j=0
    for i in range(shift_factor,len(oldarray)):
        newarray[i]=oldarray[j]
        j=j+1
    #print(newarray)
    return(newarray)
originalarray=copyarray(myarray)       #change here
newar_array=shift_right(originalarray,1)
print(newar_array)
print("112")
#inserting an elemet into an arry
print("114")
#if not empty move other one place right
#if fully filled then resize by 1
def isfilled_array(array):
    condition=True

def insert_array(array,index,item):
    if array[index]==0: #[5,5,5,0,5,5,5] i=3
        array[index]=item
        return array
    elif(array[len(array)-1]==0):   #[5,5,5,5,5,0] i=3
        #last elemet empy
        #shift one step to right
        for i in range(index,len(array)):
            #[0,1,2, 3 ,4,5,0]
            temp=array[i]
            array[i]=item
            item=









