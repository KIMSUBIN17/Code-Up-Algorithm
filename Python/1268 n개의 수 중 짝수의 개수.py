n = int(input())
numbers = map(int,input().split())
count_even = 0

for n in numbers:
    if (n % 2 == 0):
        count_even += 1 
print(count_even)
