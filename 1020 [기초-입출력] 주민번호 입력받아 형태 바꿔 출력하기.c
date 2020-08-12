#include<stdio.h>

int main()
{
	char n[15];
	int i;

	scanf("%s", &n);

	int length = strlen(n);   //strlen() 문자열 길이 구하기

	for (i = 0; i < length; i++) {
		if (n[i] == '-');
		else 
			printf("%c", n[i]);
	}

	return 0;
}
