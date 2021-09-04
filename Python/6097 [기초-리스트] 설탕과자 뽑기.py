h,w = map(int,input().split())
n = int(input())

#리스트컴프리헨션->2차원배열 생성
#가로(w), 세로(h)의 크기의 0으로 이루어진 배열 m생성
m = [[0] * w for _ in range(h)]


#n : 막대개수
for i in range(n):
	#막대길이(l), 방향(d), 좌표(x,y)입력
    l,d,x,y = map(int,input().split())
    
    for j in range(l):
	#x,y에서 1씩 빼는 이유는 입력 좌표x,y가 (0,0)이 아니라 (1,1)부터 시작하기 때문
	#d=0(가로)일 때 
        if d == 0:
            m[x-1][y-1+j] = 1 
	#d=1(세로)일 때
        else:
            m[x-1+j][y-1] = 1 
#할당한 값을 m리스트에 저장된 값들을 for문을 통해 출력
for i in range(h):
    for j in range(w):
        print(m[i][j], end=' ')
    print(end="\n")


