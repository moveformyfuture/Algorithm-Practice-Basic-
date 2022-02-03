
#34번 정수 2개 입력받아 차 계산하기
a, b=input().split() #입력받은 정수를 split의("구분")을 기준으로 자름
c=int(a)-int(b)
print(c)

#35번 실수 2개 입력받아 곱 계산하기
a, b=input().split() #입력받은 정수를 split의("구분")을 기준으로 자름
c=float(a)*float(b)
print(c)

#36번 단어 여러번 출력하기
a, b=input().split()
c=a*int(b)
print(c)

#37번 문장 여러번 출력하기
a, b=input(), input()
c=int(a)*b
print(c)

#38번 정수 2개 입력받아 거듭제곱 계산하기
a, b=input().split()
c=int(a)**int(b)
print(c)

#39번 실수 2개 입력받아 거듭제곱 계산하기
a, b=input().split()
c=float(a)**float(b)
print(c)

#40번 정수 2개 입력받아 몫 계산하기
a, b=input().split()
c=int(a)//int(b)
print(c)

#41번 정수 2개 입력받아 나눈 나머지 계산하기
a, b=input().split()
c=int(a)%int(b)
print(c)

#42번 실수 1개 입력받아 소숫점 이하 자리 변환하기
a=float(input())
b=format(a,".2f") #a를 반올림하여 소수점 2째 자리까지 나타내기
print(b)
