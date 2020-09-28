n = int(input())

a = oct(n)
b = hex(n)

print(a[2:],b[2:].upper())

#.upper : 소문자 -> 대문자
