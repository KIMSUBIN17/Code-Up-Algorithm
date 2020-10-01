#include <stdio.h>

int main(void){
    int a,c;
    char b;
    
    scanf("%d", &a);
    scanf("%c", &b);
    scanf("%d", &c);
    
    if(b == '+'){
    printf("%d", a+c);
    }
    if(b == '-'){
    printf("%d", a-c);
    }
    if(b == '*'){
    printf("%d", a*c);    
    }
    if(b == '/'){
    printf("%.2lf", (float)a/c);    
    } 
    
 
}
 

