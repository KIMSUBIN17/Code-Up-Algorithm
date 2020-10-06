#include <stdio.h>
#include <string.h>

int main()
{
    char a[101], b[101];

    scanf("%s", a);
    scanf("%s", b);
    //strlen():문자열의 길이 알려줌
    if (strlen(a) < strlen(b))
    {
        printf("%s %s", a, b);
    }
    else if (strlen(a) > strlen(b))
    {
        printf("%s %s", b, a);
    }
    else
    {
        if (strcmp(a, b) < 0)
        {
            printf("%s %s", a, b);
        }
        else
        {
            printf("%s %s", b, a);
        }
    }

    return 0;
}
//strcmp():두 개의 문자열 비교
//정확하게 일치 or 다르다면 어떤 문자열이 사전적 순서로 앞에 있는지 알려줌
