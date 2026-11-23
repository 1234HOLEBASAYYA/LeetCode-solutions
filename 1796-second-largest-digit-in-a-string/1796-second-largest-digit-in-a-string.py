class Solution:
    def secondHighest(self, s: str) -> int:
        l=[]
        m=-1
        se=-1
        for ch in s:
            if ch.isdigit():
                # l.append(int(ch))
                
                if int(ch) >m:
                    se=m
                    m=int(ch)
                elif int(ch) >se and int(ch)!=m:
                    se=int(ch)
        if se==-1:
            return -1
        else:
            return se

                


        # maximum=max(l)
        # s=0
        # for i in range(len(l)):
        #     if l[i]<maximum and i
        
        