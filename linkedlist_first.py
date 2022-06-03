#week 1 lecture sheet
#creating array
#iterating over the elements of an array
#copying an array
#resizing an array
#reversing an array
#shifing an array left
#shiffing an array right
#inserting an elemet into an arry
#removing an elemt from an array
#rotating an array left
#rotating an array right

#first of all list is not array
#u cannot expand arrray
#u cannot append array

#some basic things https://www.w3schools.com/python/python_arrays.asp

#creating an array with size array=[0]*5
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
originalarray=myarray
newar_array=resize(originalarray,5)
print(newar_array)
newar_array=resize(originalarray,-2)
print(newar_array)









