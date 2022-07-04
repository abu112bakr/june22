#        0 1 2 3 4
cir_arr=[4,0,1,2,3]

def insert(cir_arr,st,sz,elem,idx):

  lastposition=(st+sz-1)%len(cir_arr)
  idx=idx
  n_item_toshift=sz-idx
  temp=lastposition
  for j in range(0,n_item_toshift):
    cir_arr[(temp+1)%len(cir_arr)] = cir_arr[temp]
    temp=temp-1
    if temp<0:
      temp=len(cir_arr)-1
  cir_arr[idx]=elem
insert(cir_arr,2,4,100,3)
print(cir_arr)











