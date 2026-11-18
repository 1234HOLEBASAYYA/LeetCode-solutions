class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        total=0
        fre=[0]*26
        for ch in chars:
            fre[ord(ch)-ord('a')]+=1
        
        for i in range(len(words)):
            fr=fre.copy()
            flag=0
            for ch in words[i]:
                fr[ord(ch)-ord('a')]-=1
                if fr[ord(ch)-ord('a')]<0:
                    flag=1
            if flag==0:
                total+=len(words[i])
        return total






