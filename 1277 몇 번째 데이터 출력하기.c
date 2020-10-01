#include <stdio.h>

int main(void) {
	int i=0;
	int n, a;
	scanf("%d", &n);
	for(i=1;i<=n; i++ )
	{
		scanf("%d",&a);
		if(i==1) printf("%d ",a);
		if(i==n/2+1) printf("%d ",a);
		if(i==n) printf("%d",a);
				
	}
	return 0;
}
