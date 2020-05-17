#include<stdio.h>
int main(){
int i,j,n;
printf("enter the number:");
scanf("%d",&n);
for(i=n;i>=1;i--){
for(j=(-i+1);j<i;j++){
printf("%d",n-abs(j));
}
printf("\n");
}
return 0;
}
/*
Output
enter the number: 3
12321
232
3
*/
