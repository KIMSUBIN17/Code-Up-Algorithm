a,r,n = map(int,input().split())
count = 1
while (n != count):
    a *=r
    count+=1
print(a)
