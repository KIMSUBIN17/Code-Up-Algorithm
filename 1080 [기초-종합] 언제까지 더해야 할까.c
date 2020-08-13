#include <stdio.h>

int main()
{
	int a, i=1;
	int sum = 0;
	scanf("%d", &a);
	while (sum < a)
	{
		sum = sum + i;
		i++;

	}
	printf("%d", i - 1);
	return 0;
}