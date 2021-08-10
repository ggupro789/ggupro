#D2 4869 종이붙이기
#최대 넓이는 30이다.
data = [0 for _ in range(31)]
 
def dp(num):
    if not num :
        return 0
    if num == 1:
        return 1
    if num == 2:
        return 3
    if not data[num]:
        data[num] = dp(num-1) + 2*dp(num-2) 
 
    return data[num]
 
T = int(input())
for t in range(1, T+1):
    N = int(input())//10
    print('#{} {}'.format(t, dp(N)))
#-----------------------------------------------------------------
def sw_stack(N):
    list = []
    count = 0
    while sum(list) < N:
        list.append(10)

    small_get = len(list)
    middle_get = 0

    # while True :
    #     list.pop()
    #     small_get -= 1
    #     if(len(list)==0):
    #         break

    #     list.append(20)

    #     if(sum(list)>N):
    #         list.pop()
    #     elif(sum(list) == N):
    #         count += (small_get+middle_get)*(middle_get


test_case = int(input())

for _ in range(test_case):
    N = list(map(int(input())))

small_rec = 10
middle_rec = 20

middle_get = 0
