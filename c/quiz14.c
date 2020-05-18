#include<stdio.h>
int main(){
int i,j=3;
float k=7;
i = k % j;// error invalid operands to binary % (have ‘float’ and ‘int’)
printf("%d",i);
return (0);
}
// compile time error
