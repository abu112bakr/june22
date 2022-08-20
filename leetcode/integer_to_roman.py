class Solution:
    def intToRoman(self, num: int) -> str:
        if num==1:
            return "I"
        n=[]
        #num=num
        num=str(num)
        #
        
        if len(num)==4:
            #
                
            n.append(int(num[0])*1000)
            n.append(int(num[1])*100)
            n.append(int(num[2])*10)  
            n.append(int(num[3]))
        elif len(num)==3:
            n.append(int(num[0])*100)
            n.append(int(num[1])*10)
            n.append(int(num[2]))
        elif len(num)==2:
            if num=="40":
                return "XL"
            elif num=="90":
                return "XC"
            else:
                n.append(int(num[0])*10)
                n.append(int(num[1]))
        else:
            n.append(int(num[0]))
            
        #for i in temp:    
        #    n.append(int(i))
        #index=0
        string=""
        #print(n)  #################
        for i in range(0,len(n)):
            if n[i]==1:
                string=string+"I"
            if n[i]==2:
                string=string+"II"
            if n[i]==3:
                string=string+"III"
            if n[i]==4:
                string=string+"IV"
            
            if n[i]==5:
                string=string+"V"
            if n[i]==6:
                string=string+"VI"
            if n[i]==7:
                string=string+"VII"
            if n[i]==8:
                string=string+"VIII"

                
            if n[i]==9:
                string=string+"IX"
            if n[i]==10:
                string=string+"X"
            if n[i]==11:
                string=string+"XI"
            if n[i]==12:
                string=string+"XII"
            if n[i]==13:
                string=string+"XIII"
            if n[i]==14:
                string=string+"XIV"
            if n[i]==15:
                string=string+"XV"
            if n[i]==16:
                string=string+"XVI"
            if n[i]==17:
                string=string+"XVII"
            if n[i]==18:
                string=string+"XVIII"
            if n[i]==19:
                string=string+"XIX"

            if n[i]==20:
                string=string+"XX"
            if n[i]==30:
                string=string+"XXX"
                #if n[i]==40:
                #string=string+"XL"
            #if n[i]==50:
            #    string=string+"L"
            if n[i]==60:
                string=string+"LX"
            if n[i]==70:
                string=string+"LXX"
            if n[i]==80:
                string=string+"LXXX"
                #if n[i]==90:
                #string=string+"XC"

                
            if n[i]==40:
                string=string+"XL"
            if n[i]==90:
                string=string+"XC"
            if n[i]==400:
                string=string+"CD"
            if n[i]==900:
                string=string+"CM"
            
            #if n[i]==1:
            #    string=string+"I"
            #if n[i]==5:
            #    string=string+"V"
            #if n[i]==10:
            #    string=string+"X"
            if n[i]==50:
                string=string+"L"
            if n[i]==100:
                string=string+"C"
            if n[i]==500:
                string=string+"D"
            if n[i]==1000:
                string=string+"M"
            
            if n[i]==200:
                string=string+"CC"
            if n[i]==300:
                string=string+"CCC"
            #if n[i]==500:
            #    string=string+"D"
            if n[i]==600:
                string=string+"DC"
            if n[i]==700:
                string=string+"DCC"
            if n[i]==800:
                string=string+"DCCC"
            #if n[i]==200:
            #    string=string+""
            if n[i]==2000:
                string=string+"MM"
            if n[i]==3000:
                string=string+"MMM"

                
        return string
            
#h=Solution()
#print(h.intToRoman(11))