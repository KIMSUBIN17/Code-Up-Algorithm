a=input()
b=input().split()

n=int(a)

#파이썬에서는 배열의 비어있는 공간 미리 확보 불가
#   => 필요한 갯수만큼 '어떤값'으로 초기화 시켜줘야함
arr=[]
for i in range(24) :  
    arr.append(0)   #append() : 리스트에 추가_0~23번지까지 0으로 채워짐
for i in range(n) :
    arr[int(b[i])]+=1    
    #호출되는 번호(주소값)을 기존 값에서 +1하여 저장
    #해당 번호가 몇번 호출 되었는지 카운트
    
for i in range(1, 24) :
    print(arr[i], end=' ')

