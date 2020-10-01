start, end = input().split()
start = ord(start)
end = ord(end)

for i in range(start, end+1):
    print(chr(i), end=' ')
