#Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#Symbol       Value
#I             1
#V             5
#X             10
#L             50
#C             100
#D             500
#M             1000
#For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

#Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

#I can be placed before V (5) and X (10) to make 4 and 9. 
#X can be placed before L (50) and C (100) to make 40 and 90. 
#C can be placed before D (500) and M (1000) to make 400 and 900.

#Runtime: 100 ms, faster than 15.19% of Python3 online submissions for Roman to Integer.
#Memory Usage: 14 MB, less than 31.05% of Python3 online submissions for Roman to Integer.





class Solution:
    def romanToInt(self, s: str) -> int:
        val=0
        #I=1
        #V=5
        #X=10
        #L=50
        #C=100
        #D=500
        #M=1000
        string=s
        s=[]
        for i in string:
            
            s.append(i)
#        #count=0
        string=0
        for i in range(0,len(s)):
          #
          next=i+1
          if next<len(s):
              if s[i]=="I" and s[next]=="V":
                  val+=4
                  s[i]=0
                  s[next]=0
              if s[i]=="I" and s[next]=="X":
                  val+=9
                  s[i]=0
                  s[next]=0
              if s[i]=="X" and s[next]=="L":
                  val+=40
                  s[i]=0
                  s[next]=0
              if s[i]=="X" and s[next]=="C":
                  val+=90
                  s[i]=0
                  s[next]=0
              if s[i]=="C" and s[next]=="D":
                  val+=400
                  s[i]=0
                  s[next]=0
              if s[i]=="C" and s[next]=="M":
                  val+=900
                  s[i]=0
                  s[next]=0
                
            #print("i {}, next {}".format(i,next))
            
#            if count <len(s)-1:
#                pass
#            count+=1
        
        #val=0
        #if "IV" in s:
        #    return 4
        #if "IX" in s:
        #    return 9
        #if "XL" in s:
        #    return 40
        #if "XC" in s:
        #    return 90
        #if "CD" in s:
        #    return 400
        #if "CM" in s:
        #    return 900
        for i in s:
            #
            if i=="I":
                val+=1
            if i=="V":
                val+=5
            if i=="X":
                val+=10
            if i=="L":
                val+=50
            if i=="C":
                val+=100
            if i=="D":
                val+=500
            if i=="M":
                val+=1000
        return val

        