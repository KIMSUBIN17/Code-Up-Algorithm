n = input()
numbers = list(map(int, input().split()))
max_num = 0

for number in numbers:
    if(number > max_num):
        max_num = number

print(max_num)
