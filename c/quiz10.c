#include<stdio.h>
int main(){
int b=20;
int* y=&b;
char n='A';
char* z=&n;
y[0]=z[0];
printf((*y==*z)?"True":"False");// True
}
