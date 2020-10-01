import math

current_time, score1, score2 = input().split()
current_time = int(current_time)
score1 = int(score1)
score2 = int(score2)

additional_points = (90 - current_time) / 5
additional_points = math.ceil(additional_points)
score1 += additional_points

if(score1 > score2):
    print('win')
elif(score1 < score2):
    print('lose')
else:
    print('same')
