#    0 1 2 3 4
lin_arr=[1,2,3,4,5]
st=3
sz=5

cir_arr=[0]*len(lin_arr)
temp=st
i=0
while(i<len(lin_arr)):
  cir_arr[temp]=lin_arr[i]
  temp=(temp+1)%len(cir_arr)
  i=i+1

print(cir_arr)




