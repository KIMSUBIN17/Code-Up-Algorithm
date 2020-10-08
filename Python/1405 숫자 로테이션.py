#첫째 줄에 숫자의 개수 n이 입력된다.( 1 <= n <= 1,000)
#둘째 줄에 n개의 정수 k가 공백으로 구분되어 입력된다.(1 <= k <= 1,000)
#왼쪽으로 하나씩 출력

a = int(input())
b = list(map(int, input().split()))
 
for i in range(a) : 
    for j in range(a) :
        print(b[j], end = ' ')
    print()
    for z in range(a-1) :
        temp = b[z]
        b[z] = b[z+1]
        b[z+1] = temp

