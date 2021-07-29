#sw_list2_5차시
# 그림과 같이 인덱스가 있는 10x10 격자에 빨간색과 파란색을 칠하려고 한다.
# N개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질 때, 칠이 끝난 후 색이 겹쳐 보라색이 된 칸 수를 구하는 프로그램을 만드시오.
# 주어진 정보에서 같은 색인 영역은 겹치지 않는다.

test_case = int(input())
#----------------------------------------------------- 함수 정의
def change_color(x:list,a:int,b:int,c:int,d:int,e:int): # 10*10 리스트 와 입력된 값들 인자로 받는다
    if(a <= c and b <= d):      # (a,b) 쌍이 (c,d) 보다 작을 때
        for i in range(a,c+1):
            for j in range(b,d+1):
                if(e == 1):     # 빨강 = 1
                    if(x[i][j] == 0):
                        x[i][j] = 1
                    elif(x[i][j] == 2):
                        x[i][j] = 3
                elif(e == 2):   #파랑 = 2
                    if(x[i][j] == 0):
                        x[i][j] = 2
                    elif(x[i][j] == 1):
                        x[i][j] = 3
    else:                       # (a,b) 쌍이 (c,d) 보다 클 때
        for i in range(c,a+1):
            for j in range(d,b+1):
                if(e == 1):
                    if(x[i][j] == 0):
                        x[i][j] = 1
                    elif(x[i][j] == 2):
                        x[i][j] = 3
                elif(e == 2):
                    if(x[i][j] == 0):
                        x[i][j] = 2
                    elif(x[i][j] == 1):
                        x[i][j] = 3
# --------------------------------------------- 
for z in range(test_case):
    N = int(input())
    
    r_list = [[0 for i in range(10)] for j in range(10)] # 10*10 리스트에 기본값 0
    count = 0

    for k in range(N):
        rectangle = list(map(int,input().split()))
        change_color(r_list,rectangle[0],rectangle[1],rectangle[2],rectangle[3],rectangle[4]) #반복문 통해서 0을 바꿔주고 겹치는 부분은 = 3이된다.
    
    for g in range(10):  # r_list에서 3 갯수 추출
        for l in range(10):
            if( r_list[g][l] == 3):
                count += 1

    print("#{0} {1}".format(z+1,count))