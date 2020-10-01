a,b,c,d = map(int,input().split())
count = a+b+c+d
# 0: 뒤집어지지 않은 상태, 1:뒤집어진 상태
# 뒤집어진 개수에 따라 도,개,걸,윷,모 판단

if (count == 1 ):
    print('도')
elif (count == 2 ):
    print('개')
elif (count == 3 ):
    print('걸')
elif (count == 4 ):
    print('윷')
else:
    print('모')
