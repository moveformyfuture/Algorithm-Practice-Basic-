#74번 문자 1개 입력받아 알파벳 출력하기
c=ord(input()) #문자의 정수값을 입력받음
a=ord('a') #a부터 시작하기 위해 a를 정수화
while a<=c :
    print(chr(a), end=' ')
    a=a+1

#75번 정수 1개 입력받아 그 수까지 출력하기
a=int(input())
b=0
while (a>=b) :
    print(b)
    b=b+1

#76번 정수 1개 입력받아 그 수까지 출력하기(range 사용)
n=int(input())
for i in range(n+1) : #range(n) : 0부터 n-1까지의 수열을 반환함
    print(i)

#77번 짝수 합 구하기
a=int(input())
b=0
for i in range(1,a+1) :
    if i%2==0 :
        b=b+i #0에 짝수만 더하기
print(b)

#78번 원하는 문자 입력될때까지 반복 출력하기
a=input()

while (a!='q') :
    print(a)
    a=input()
print(a)

#79번 0~1000이하까지만 계속 더하는 프로그램
a=int(input())
b=0
c=0
while (a>=b) :
    for i in range(a+1) :
        c=c+i #누적값 더하기
        b=b+1 #횟수 카운팅
        if (a<=c) :
            print(b-1)
            break
    break

#80번 주사위 2개 던지기
a, b=input().split()
a=int(a)
b=int(b)
for i in range(1, a+1) : #i부터 반복 완료
    for j in range(1, b+1) : #그다음 j 반복
        print(i,j)




