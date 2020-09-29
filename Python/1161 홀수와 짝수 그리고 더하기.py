n1,n2 = map(int,input().split())

if n1 % 2 == 0:
    if n2 % 2 ==0:
        print('짝수+짝수=짝수')
    else:
        print('짝수+홀수=홀수')
else:
    if n2 % 2 ==0:
        print('홀수+짝수=홀수')
    else:
        print('홀수+홀수=짝수')
    

