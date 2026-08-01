class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0)return false;
        long reverse=0;
        int nums=x;
        while(x!=0)
        {
            reverse=(reverse*10)+x%10;
            x=x/10;
        }
        if(reverse==nums)return  true;
        else
        return false;
    }
};