# 코딩반 학생들에게 이진 탐색을 설명하던 선생님은 이진탐색을 연습할 수 있는 게임을 시켜 보기로 했다.
# 짝을 이룬 A, B 두 사람에게 교과서에서 각자 찾을 쪽 번호를 알려주면, 이진 탐색만으로 지정된 페이지를 먼저 펼치는 사람이 이기는 게임이다.

test_case = int(input())

def search(x,y):
    start = 1
    end = x
    k_count = 0
    while start<=end:
        mid = (start + end) // 2
        k_count += 1
        if(mid == y):
            return k_count
        elif(mid < y):
            start = mid

        elif(mid > y):
            end = mid

for i in range(test_case):
    PAB = list(map(int,input().split()))
    a = search(PAB[0],PAB[1])
    b = search(PAB[0],PAB[2])
    # print(a,b)
    if( a == b):
        print("#{0} {1}".format(i+1,0))
    elif(a < b):
        print("#{0} {1}".format(i+1,'A'))
    else:
        print("#{0} {1}".format(i+1,'B'))
