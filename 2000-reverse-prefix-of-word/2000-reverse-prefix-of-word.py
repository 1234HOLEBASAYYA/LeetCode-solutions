class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index=word.find(ch)
        pre=word[:index+1]
        pre=pre[::-1]
        return pre+word[index+1:]
        
        