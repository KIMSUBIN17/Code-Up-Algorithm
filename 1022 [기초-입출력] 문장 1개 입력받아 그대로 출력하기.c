#include<stdio.h>

int main()
{
	char data[2001];
	fgets(data, 2000, stdin);  
	//fgets( ) 를 사용하면 공백문자가 포함되어있는 문장을 입력받아 저장
	//scanf() 를 이용하면, 첫 번째 단어까지만 저장
	printf("%s", data);

	return 0;

}
