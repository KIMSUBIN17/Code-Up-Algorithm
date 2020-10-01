startnum,lastnum = input().split()
startnum = int(startnum)
lastnum = int(lastnum)

for i in range(startnum, lastnum + 1):
    if(i % 2 == 1):
        print(i, end=' ')
