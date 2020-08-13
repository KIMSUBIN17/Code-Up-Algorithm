#include <stdio.h>

int main()
{
	char a;
	while (a != 'q')
	{
		scanf("%s", &a);
		printf("%c\n", a);
	}
	return 0;
}