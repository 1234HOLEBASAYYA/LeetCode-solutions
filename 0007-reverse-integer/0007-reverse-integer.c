int reverse(int x){
    int n=x;
int reverse=0;
while(x!=0)
{
    int digit=x%10;
    if(reverse<INT_MIN/10||reverse>INT_MAX/10)return 0;
    
        reverse=reverse*10+digit;
        x=x/10;
        // if(n<0)reverse=-reverse;
    
    
}
// if(n<0)reverse=-reverse;
return reverse;
}