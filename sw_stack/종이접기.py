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
