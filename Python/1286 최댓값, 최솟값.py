numbers = []

for i in range(0, 5):
    number = input()
    numbers.append(int(number))

numbers.sort()
    
print(numbers[len(numbers) - 1])   #최댓값
print(numbers[0])                   #최솟값

