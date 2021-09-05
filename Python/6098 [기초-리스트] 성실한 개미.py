#(2,2)에서 시작, 오른쪽에 1이 없을때까지 오른쪽으로 이동
#오른쪽=1이면 아래로 이동
#현재위치를 9로 바꿈
#2를 만나면 9로 바꿈
#개미는 오른쪽(y+1)이나 아래(x+1)로만 이동
#반복문 탈출조건:y+1과 x+1이 모두 1 or 먹이를 먹은 경우

1. 2차원 배열 arr 생성
2. while문 
  1) 현재칸이 0이면 9로 변환, 현재칸이 2이면 9로 변환 후 반복문 종료
  2) 오른쪽과 아래가 모두 1이면 종료
  3) 오른쪽이 1이 아니면 y증가시킴, 오른쪽이 1이고 아래쪽이 1이 아니라면 x증가

arr = []
for i in range(10):
    arr.append(list(map(int, input().split())))
    
x, y = 1, 1

while True:
    if arr[x][y] == 0: # 갈 수 있는 곳은 9로 표시
        arr[x][y] = 9
    elif arr[x][y] == 2: # 먹이를 먹으면 9로 표시 & 이동X
        arr[x][y] = 9
        break
    
    if ((arr[x][y+1] == 1 and arr[x+1][y] == 1) or (x==9 and y==9)):
        break #  맨 아래의 가장 오른쪽에 도착한 경우 & 더이상 움직일 수 없음
    
    if arr[x][y+1] != 1: # 오른쪽으로 이동 시
        y += 1
    elif arr[x+1][y] != 1: # 아래쪽으로 이동 시
        x += 1
        
for i in range(10):
    for j in range(10):
        print(arr[i][j], end=' ')
    print()
