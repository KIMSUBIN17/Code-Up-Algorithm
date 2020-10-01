a,b,c = map(int,input().split())

if(a<=170):
    print('CRASH ' + str(a))
    
elif(b<=170):
    print('CRASH ' + str(b))
    
elif(c<=170):
    print('CRASH ' + str(c))
else:
    print('PASS')
