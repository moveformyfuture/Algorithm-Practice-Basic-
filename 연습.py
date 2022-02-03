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