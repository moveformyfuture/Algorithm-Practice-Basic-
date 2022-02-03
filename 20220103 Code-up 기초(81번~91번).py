#81번 16진수 구구단 출력하기

a=input()
a=int(a, 16) #입력받은 a를 16진수로 저장하기
b=1

while (b<16) :
    c=a*b
    print('%X'%a, '*', '%X'%b, "=", '%X'%c, sep='')
    b=b+1

#82번 369 게임 프로그램 짜기
a=int(input())

for i in range(a+1) :
    if (i%10==3) :
        print('X', end=' ')
    elif (i%10==6) :
        print('X', end=' ')
    elif (i%10==9):
        print('X', end=' ')
    elif (i==0) :
        continue
    else :
        print(i,end=' ')

#83번 빛 섞을 수 있는 경우의 수
r, g, b=input().split()
r=int(r)
g=int(g)
b=int(b)

for ri in range(r) :
    for gi in range(g) :
        for bi in range(b) :
            print(ri, gi, bi, sep=' ')
print(r*g*b)

#84번 소리 파일 저장용량 계산하기
h, b, c, s=input().split()
h, b, c, s=int(h), int(b), int(c), int(s)

a=h*b*c*s/8/1024/1024
a=float(a)
a=format(a, ".1f")
print(a, "MB")

#85번 그림파일 저장용량 계산하기
w, h, b=input().split()
w, h, b=int(w), int(h), int(b)

a=w*h*b/8/1024/1024
a=float(a)
a=format(a, ".2f")
print(a, "MB")

#86번 거기까지! 이제 그만~
a=int(input())
b=0
while True :
    for i in range(a+1) :
        b=b+i #누적값 더하기
        if (b>=a) :
            print(b)
            break
    break

#87번 3의 배수는 통과
a=int(input())

for i in range(a+1) :
    if (i==0) :
        continue
    elif (i%3==0) :
        continue
    else :
        print(i, end=' ') #end : 붙여주기

#88번 수 나열하기 1
a, d, n=input().split()
a,d,n=int(a), int(d), int(n)

f=(n-1)*d+a
print(f)

#89번 수 나열하기2
a, r, n=input().split()
a,r,n=int(a), int(r), int(n)

f=a*(r**(n-1)) # ** : 제곱
print(f)

#90번 수 나열하기3
a, m, d, n=input().split()
a,m,d, n=int(a), int(m), int(d), int(n)

b=1

while (b<=n):
    f = a * m + d
    a=f
    b=b+1
    if (b==n):
        print(f)
    if (b==2 and n==1) :
        print(1)

#91번 함께 문제 푸는 날
a, b, c=input().split()
a, b, c=int(a), int(b), int(c)

d=1
while True :
    d=d+1
    if (d%a==0 and d%b==0 and d%c==0) :
        print(d)
        break
