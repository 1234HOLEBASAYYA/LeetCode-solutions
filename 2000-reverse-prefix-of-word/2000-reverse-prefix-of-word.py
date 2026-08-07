class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index=-1
        for i in range(len(word)):
            if word[i]==ch:
                index=i
                break
        prefix=word[0:index+1]
        rev=prefix[::-1]
        if index==-1:
            return word
        else:
            return rev+word[index+1:]