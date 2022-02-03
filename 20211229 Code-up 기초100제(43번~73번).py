#43번 실수 2개 입력받아 나눈 몫 계산하기
a, b=input().split()
a, b=format(float(a), '3f'), format(float(b), '3f')
c=float(a)/float(b)
c=format(c, ".3f")
print(c)

#44번 정수 2개 입력받아 자동 계산하기
a, b=input().split()
a, b=int(a), int(b)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
c=float(a)/float(b)
c=format(c, ".2f")
print(c)

#45번 정수 3개 입력받아 합과 평균 출력하기
a, b, c=input().split()
a, b, c=int(a), int(b), int(c)
plus=a+b+c
avg=plus/3
print(plus, format(avg, ".2f"))

#46번 정수 1개 입력받아 2배 곱해 출력하기
a=int(input())
print(a<<1) #비트시프트 사용 (<< : 2배 증가, >> : 2배 감소)

#47번 2의 거듭제곱 배로 곱해 출력하기
a, b=input().split()
a, b= int(a), int(b)
print(a<<b)

#48번 정수 2개 입력받아 대소 비교하기
a, b=input().split()
a, b=int(a), int(b)
print(a<b)

#49번 정수 2개 입력받아 대소 비교하기
a, b=input().split()
a, b=int(a), int(b)
print(a==b)

#50번 정수 2개 입력받아 대소 비교하기
a, b=input().split()
a, b=int(a), int(b)
print(a<=b)

#51번 정수 2개 입력받아 대소 비교하기
a, b=input().split()
a, b=int(a), int(b)
print(a!=b)

#52번 정수 입력받아 참 거짓 평가하기
a=int(input())
print(bool(a)) #bool : 참이면 True, 거짓이면 False 반환

#53번 정수 입력받아 참 거짓 바꾸기
a=int(input())
print(bool(not a)) #bool : 참이면 True, 거짓이면 False 반환

#54번 둘다 참일 경우에만 출력하기
a, b=input().split()
a, b=int(a), int(b)
a, b=bool(a), bool(b)
print(a and b) # and : 둘다 true일때만 true를 반환. 나머지는 false

#55번 하나라도 참일 경우에만 출력하기
a, b=input().split()
a, b=int(a), int(b)
a, b=bool(a), bool(b)
print(a or b) # and : 하나라도 true일때 true를 반환.

#56번 참/거짓이 서로 다를때에만 참 출력하기
a, b=input().split()
a, b=int(a), int(b)
a, b=bool(a), bool(b)
print((a and not b) or (not a and b))

#57번 참/거짓이 서로 같을 때에만 참 출력하기
a, b=input().split()
a, b=int(a), int(b)
a, b=bool(a), bool(b)
print((a and b) or (not a and not b))

#58번 둘다 거짓일 때에만 참 출력하기
a, b=input().split()
a, b=int(a), int(b)
a, b=bool(a), bool(b)
print(not a and not b)

#59번 비트단위로 Not하여 출력하기
a=int(input())
print(~a) #~ : a를 2진수로 바꿔서 보수법을 취한 후 -1을 한다. ~n : -n-1

#60번 비트단위로 & 연산하여 출력하기
a, b=input().split()
a,b=int(a), int(b)
print(a&b) #& : 2진수로 변환했을때 같은 위치에 1인 것만 남긴다.

#61번 비트단위로 or 하여 출력하기
a, b=input().split()
a,b=int(a), int(b)
print(a|b) #| : 2진수로 변환했을때 하나라도 1이면 1로 변환한다.

#62번 비트단위로 Xor하여 출력하기
a, b=input().split()
a,b=int(a), int(b)
print(a^b) #^ : xor을 의미. 서로 다른 부분만 골라내 1로 변환한다.

#63번 3항연산 활용해 정수 2개 입력받아 큰값 출력하기.
a, b=input().split()
a,b=int(a), int(b)
c=(a if (a>b) else b)
print(c)

#64번 3항연산, 정수 3개 입력받아 가장 작은 값 출력하기.
a, b, c=input().split()
a,b,c=int(a), int(b), int(c)
d= (a if (a<b) else b)
e= d if (d<c) else c
print(e)

#65번 정수 3개 입력받아 짝수만 출력하기.
a, b, c=input().split()
a,b,c=int(a), int(b), int(c)
if a%2==0 : print(a)
if b%2==0 : print(b)
if c%2==0 : print(c)

#66번 정수 3개 입력받아 짝/홀 출력하기
a, b, c=input().split()
a,b,c=int(a), int(b), int(c)
if a%2==0 : print("even")
else : print("odd")
if b%2==0 : print("even")
else : print("odd")
if c%2==0 : print("even")
else : print("odd")
# if-else 구조 중요

#67번 정수 1개 입력받아 분류하기
a=int(input())
if a<0 and a%2==0 : print("A")
if a<0 and a%2!=0 : print("B")
if a>0 and a%2==0 : print("C")
if a>0 and a%2!=0 : print("D")

#68번 점수 입력받아 평가 출력하기
a=int(input())
if (90<=a<=100) : print("A")
if (70<=a<=89) : print("B")
if (40<=a<=69) : print("C")
if (0<=a<=39) : print("D")

#69번 평가 입력받아 다르게 출력하기(elif문)
a=input()
if (a=='A') : print("best!!!") #else가 없으면 이것만 실행하고 끝나버림
elif (a=='B') : print("good!!")
elif (a=='C') : print("run!")
elif (a=='D') : print("slowly~")
else : print("what?")

#70번 월 입력받아 계절 출력하기 (수의 특징 관찰)
a=int(input())
if (a//3==1) : print("spring")
elif (a//3==2) : print("summer")
elif (a//3==3) : print("fall")
else : print("winter")

#71번 0 입력될때까지 무한 출력하기(반복문)
n=1 #처음 조건 검사를 통과하기 위해 0이 아닌 값을 임의로 저장
while n!=0 :
    n=int(input())
    if (n!=0) : print(n)

#72번 정수 1개 입력받아 카운트다운 출력하기
a = int(input())
print(a)
while a!=1 :
    a=a-1
    print(a)

#73번 정수 1개 입력받아 카운트다운 출력하기
a = int(input())
while a!=0 :
    a=a-1
    print(a)

#74번 문자 1개 입력받아 알파벳 출력하기
a=ord(input()) #문자의 정수값을 입력받음
while (a!=1) :
    b=ord('a') #문자a를 숫자로 변환하여 b에 저장
    b=b+1
    b=chr(b)
    print(b)





