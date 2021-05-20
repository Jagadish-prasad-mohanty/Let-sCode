def findNth(N):
        #code here
        res=0
        start=1
        
        while(N>0):
            res+=start*(N%9)
            
            N//=9
            start*=10
            
        return res

print(findNth(99))