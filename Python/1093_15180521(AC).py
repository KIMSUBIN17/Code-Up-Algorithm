n = int(input())
array = list(map(int,input().split()))
all = [0]*23
for i in array :
    all[i-1] += 1
for j in all :
    print(j,end=" ")

