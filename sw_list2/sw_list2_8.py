# 보통의 정렬은 오름차순이나 내림차순으로 이루어지지만, 이번에는 특별한 정렬을 하려고 한다.
# N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬하는 방법이다.

test_case= int(input())

def bungara(x:list,y:list): # 번갈아 저장해줄 함수
    i = 0
    result_list = []
    while i < len(x):
        result_list.append(x[i])
        result_list.append(y[i])
        i += 1

    return result_list

for i in range(test_case):
    N = int(input())
    N_list = list(map(int,input().split()))
    N_list_1 = sorted(N_list,reverse=True)[:N//2]  #홀수는 배제
    N_list_2 = sorted(N_list)[:N//2]

    result = bungara(N_list_1,N_list_2)
    print("#{0}".format(i+1),end=' ')

    for i in range(10):
        if(i != 9):
            print("{0}".format(result[i]),end=' ')
        else:
            print("{0}".format(result[i]))
