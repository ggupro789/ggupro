#sw_list1_7차시 문제

lines = int(input()) #노선 수


for i in range(lines):
    KNM = list(map(int,input().split(' ')))
    # k =  한 번에 최대 이동할 수 있는 정류장
    # N =  종점 정류장
    # M =  충전기 잇는 정류장 수

    where_m = list(map(int,input().split(' ')))
    max_k = 0 # 이동할 수 있는 정류장까지 제일 근접한 값
    count = 0 # 횟수 카운트
    set_k = [] # max_k 값 추출하기 위해 필요한 리스트

    while (KNM[0]+max_k <KNM[1]):
        set_k = [i for i in where_m if(max_k< i <= KNM[0]+max_k)]
    
        try:
            max_k = max(set_k)
        except ValueError: # set_k 에 값 없으면 중간이 비게된다는 뜻으로 종점까지 못감
            count = 0
            break

        count += 1

    print("#{0} {1}".format(i+1, count))