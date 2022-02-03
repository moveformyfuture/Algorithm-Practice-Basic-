#92번 이상한 출석 번호 부르기1
n=int(input()) #출석을 n번 부름
a=input().split() #n번 부른 각각의 개별 번호들을 list형태로 받음

for i in range(n) : #0부터 n-1까지 수 나열
    a[i]=int(a[i]) #a의 리스트 숫자 각각을 int로 정수화
d=[] #d라는 비어있는 리스트 생성 --> 카운트 값을 세기 위해 만듦
for i in range(24) :
    d.append(0) #리스트 d의 마지막에 0을 추가 --> for문으로 반복되어 0이 계속 추가됨.
for i in range(n) :
    d[a[i]]+=1 #리스트 a의 count누적값을 d에 저장해줌
for i in range(1,24) :
    print(d[i], end=' ') #count가 누적된 리스트 d를 출력

#92번 이상한 출석 번호 부르기2
n=int(input()) #출석을 n번 부름
a=input().split() #n번 부른 각각의 개별 번호들을 list형태로 받음.
a.reverse() #list를 역으로 호출해 저장하는 함수

for i in range(n) :
    a[i]=int(a[i]) #list형식을 int형식으로 바꿔주기
    print(a[i], end=' ') #int형식의 a를 한칸 띄워서 출력

#94번 이상한 출석 번호 부르기3
n=int(input())
a=input().split()

for i in range(n) :
    a[i]=int(a[i])
min=a[0]
for i in range(0,n):
    if a[i]<min :
        min=a[i]
print(min)

#95번 바둑판에 흰 돌 놓기

# 0으로 구성된 X, Y축의 리스트 생성
d=list()
for i in range(20):
    d.append(list()) # 리스트 안에 리스트 추가하기
    for j in range(20):
        d[i].append(0)

# (X, Y) 값을 입력받아 1로 표현하도록 만들기
n=int(input())
for i in range(n): #(X, Y)를 n번 반복해서 입력하도록 구현
    x, y=input().split()
    d[int(x)][int(y)]=1

for i in range(1, 20) :
    for j in range(1, 20) :
        print(d[i][j], end=' ')
    print() #줄바꿈

#96번 바둑판에 흰 돌 놓기
# 이중 리스트를 활용해 0이 채워진 (19, 19) 바둑판 만들기

d = list((list(map(int, input().split()))) for _ in range(19)) #d를 이중리스트로 만들기 - [i for i in range]
n = int(input())

for i in range(n):
    x, y = map(int, input().split()) #x좌표, y좌표
    x -= 1
    y -= 1
    for j in range(19):
        if d[j][y] == 0:
            d[j][y] = 1
        else:
            d[j][y] = 0

        if d[x][j] == 0:
            d[x][j] = 1
        else:
            d[x][j] = 0

for i in range(19):
    print(*d[i]) #행별로 unpacking해서 출력 대입받는거에서는 패킹, 이미 있는거는 언패킹

#97번 설탕과자 뽑기

h, w = map(int, input().split()) #바둑판 크기 입력

shape = [[0] * w for _ in range(h)] #바둑판 생성 :

n = int(input()) #막대의 개수 입력받음

for i in range(n):
    l, d, x, y = map(int, input().split())
    if d == 0: #가로로 놓인 막대의 길이만큼 1로 변환
        for j in range(l):
            shape[x - 1][y - 1 + j] = 1
    else: #세로로 놓인 막대의 길이만큼 1로 변환
        for j in range(l):
            shape[x - 1 + j][y - 1] = 1

for i in range(h): #격자는 세로 먼저
    for j in range(w): #격자는 가로를 나중에
        print(shape[i][j], end=' ') #end=' ' : 한칸 띄어쓰기 후 출력해줌
    print() #반복이 끝나면 줄바꿔줌

# 98번 성실한 개미
# 리스트를 입력받는 템플릿(리스트 함수로 쓸때 묶어줘야한다고 생각해야 함)
shape = list((list(map(int, input().split()))) for _ in range(10))

# 초기좌표 설정
x=1
y=1

#좌표이동
while True :
    if shape[x][y]==0 :
        shape[x][y]=9
        y=y+1
    elif shape[x][y]==1 :
        x=x+1
        y=y-1
        if shape[x][y]==0 :
            shape[x][y]=9
            y=y+1
        elif shape[x][y]==2 :
            shape[x][y] = 9
            break
        elif shape[x][y]==1 :
            break
    elif shape[x][y] == 2:
        shape[x][y] = 9
        break

#이중리스트의 출력 템플릿
for i in range(10):
    for j in range(10):
        print(shape[i][j], end = ' ')
    print()
