  def printFullLinear(self): 
    for i in range(0,len(self.cir)-1):
      print(self.cir[i])
  def printForward(self): #Easy           #DONE 2 
    i=self.start
    count=0
    while count<(self.size):
      print(self.cir[i])
      
      count+=1
      i=(i+1)%len(self.cir)
    
  
  def printBackward(self):
    i=(self.start+self.size-1)%len(self.cir)
    count=0
    while count<(self.size):

      print(self.cir[i])
      i=i-1
      count+=1
      if i<0:
        i=len(self.cir)-1
  def linearize(self):
    new_array=[0]*self.size
    i=self.start
    count=0
    while count<(self.size):
      new_array[count]=self.cir[i]
      
      count+=1
      i=(i+1)%len(self.cir)    
    print("new linear array #")
    print(new_array)