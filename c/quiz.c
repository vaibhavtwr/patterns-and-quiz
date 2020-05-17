#include<stdio.h>
int main(){
char str1[] = "Codeknow";
char str2[] = {'c','o','d','e','k','n','o','w'};
int n1 = sizeof(str1) / sizeof(str1[0]);
int n2 = sizeof(str2) / sizeof(str2[0]);
printf("n1 = %d , n2 = %d",n1,n2);
return 0;
}
/*
Output:
n1 = 9 , n2 = 8
*/
