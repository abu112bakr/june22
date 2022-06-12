def find_same(a):
  for i in range(0,len(a)):
    print(i)
    
    for j in range(i+1,len(a)):
      print(j,end=" ")
      if a[i]==a[j]:
        print()
        print(a[i]," matches")
    print()
a=[1,5,6,8,5]
a=[1,3,6,8,7]
a=[1,4,1,6,8,5]
find_same(a)

