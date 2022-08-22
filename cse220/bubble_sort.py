a=[5,1,9,-3]
i=0
j=1
print(a)
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[j]<a[i]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print(a)