str = input()

for i in range(0, len(str)):  #str길이만큼 반복
    if str[i] == 't':           #반복중에 str중 t가 들어간 곳이 있으면
        print(i+1,end=' ')      
        #줄바꿈없애기 위해 end=''추가, 0부터 시작하기 때문에 위치출력위해 +1
