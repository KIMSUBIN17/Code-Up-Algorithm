y, m, d = map(int,input().split())

n = (y + m + d) % 1000  # %는 나머지
n = int(n / 100)        # /은 나누기

if n % 2 == 0:
    print('대박')
else:
    print('그럭저럭')
