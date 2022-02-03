

#11번 실수 1개 입력받아 변환하여 출력하기

x = input() #input으로 넣는 입력값은 무조건 문자형자료형으로 들어간다.
print(x)


#12번 정수 두개를 입력받아 그대로 출력하기
a = input()
a=int(a)
b = input()
b=int(b)
print(a)
print(b)

x ,y = int(input()), int(input())
print(x,y)

#13번 문자 2개 입력받아 순서 바꿔 출력하기
a, b = input(),  input() # 문자 입력받기(자료형 상관없음)
print(b,a) #b, a 순으로 출력

#14번 실수 1개 입력받아 3번 출력하기

a=float(input())
print(a)
print(a)
print(a)

#15번 공백을 두고 입력된 정수 2개를 입력받아 따로 출력하기
a, b = input().split() #입력받은 정수를 공백을 기준으로 자름
a=int(a)
b=int(b)
print(a)
print(b)

#16번 공백을 두고 문자 2개를 입력받아 순서를 바꿔 출력
a, b = input().split() #입력받은 정수를 split의("구분")을 기준으로 자름
print(b, a)

#17번 입력받은 문장을 3번 출력
a=input()
print(a,a,a)

#18번 시:분 형식으로 출력하기
a, b = input().split(':') # ':' 기준으로 나누겠다.
print(a, b, sep=':') # ':' 으로 구분하여 출력하겠다.

#19번 연월일 입력받아 순서 바꿔 출력하기
y, m, d = input().split('.') # ':' 기준으로 나누겠다.
print(d, m, y, sep='-') # '-' 으로 구분하여 출력하겠다.

#20번 주민번호 이어붙여 출력하기.
a, b=input().split('-')
print(a+b)

#21번 단어 스펠링 나누어 출력하기
a=input()
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

#22번 연월일을 공백 포함 한줄로 출력하기
ymd=input()
print(ymd[0:2])
print(ymd[2:4])
print(ymd[4:6])

#23번 시:분:초 에서 분만 출력하기
y, m, d=input().split(':')
print(m)

#24번 공백이 있는 단어 이어붙여 출력하기
a, b=input().split()
print(a+b)

#25번 두 정수의 합을 출력하기
a, b=input().split()
print(int(a)+int(b))

#26번 실수 2개 입력받아 합으로 출력하기
a, b=float(input()), float(input())
print(a+b)

#27번 10진수 정수를 입력받아 16진수로 출력하기
a=int(input())
print('%x'% a) #a에 저장된 정수를 x(16진수를 나타냄)으로 출력

#28번 10진수 정수를 입력받아 16진수 대문자로 출력하기
a=int(input())
print('%X'% a) #a에 저장된 정수를 X(16진수 대문자로 나타냄)으로 출력

#29번 16진수를 입력받아 8진수로 출력하기
a=input()
a=int(a, 16) #입력받은 a를 16진수로 저장하기
print('%o'%a) #a를 o(8진수)로 출력하기

#30번 영문자 1개를 입력받아 10진수로 변환하기
a=input()
a=ord(a) #입력받은 a를 10진수 유니코드값으로 변환한다. (ordinal position)
print(a)

#31번 10진수를 입력받아 영문자(유니코드로 출력하기)
a=int(input())
a=chr(a) #입력받은 a를 유니코드값으로 변환한다. (character)
print(a)

#32번 정수를 입력받아 부호를 바꿔서 출력한다.
a=int(input())
print(-a)

#33번 문자를 입력받아 다음 문자를 출력하기
input_a=input() #문자를 입력받기
trans_a=ord(input_a) #입력받은 a를 10진수 유니코드값으로 변환한다. (ordinal position)
b=trans_a+1
b=chr(b) #입력받은 a를 유니코드값으로 변환한다. (character)
print(b)

