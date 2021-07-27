#sw_list1_7차시 문제

lines = int(input()) #노선 수


for i in range(lines):
    KNM = list(map(int,input().split(' ')))
    # k =  한 번에 최대 이동할 수 있는 정류장
    # N =  종점 정류장
    # M =  충전기 잇는 정류장 수

    where_m = list(map(int,input().split(' ')))    