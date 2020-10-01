n = int(input())
isPrime = 'prime'

for i in range(2,n):
    if n % i == 0:
        isPrime = 'not prime'
        break
print(isPrime)
