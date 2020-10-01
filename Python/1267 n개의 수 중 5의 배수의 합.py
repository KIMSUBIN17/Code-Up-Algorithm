n = int(input())
numbers = map(int,input().split())
sum = 0

for n in numbers:
    if (n % 5 == 0):
        sum+=n 
print(sum)
