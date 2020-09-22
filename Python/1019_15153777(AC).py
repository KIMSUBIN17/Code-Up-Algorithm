#입력 시 연, 월, 일이 "."으로 구분
#출력 시yyyy.mm.dd 형식으로 출력
#%02d를 사용하면 2칸을 사용해 출력하는데,한 자리 수인 경우 앞에 0을 붙여 출력한다.)

year, month, day = input().split('.')
print(year.zfill(4), month.zfill(2), day.zfill(2), sep = '.')


#sep 옵션 :띄어쓰기(공백) 말고 다른 문자를 넣기 가능

# .zfill 함수 : 자릿수 맞추기
