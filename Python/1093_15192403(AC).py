n = int(input())
rand = map(int, input().split())
student = [0 for _ in range(23)]
for r in rand:
  student[r-1] += 1
print(*student)
#ex)print([1,2,3)>>[1,2,3]  -- 리스트형태로 출력
#ex)print(*[1,2,3])>>1 2 3  -- 내부의 원소 그대로 출력(리스트형태X)
