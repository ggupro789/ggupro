def my_combination(list:list, k, r,count):
    if list.count(1) == r:
        #탈출
        print(list)
        return

    if k > 3: #  k의 역활 이해
        return

    my_combination(list,k+1,r,count)
    my_combination(list.insert(k,1),k+1,r,count+1)


N,M,D = map(int,input().split())

map_list = [list(map(int,input().split())) for _ in range(N)]
row_list = [0 for _ in range(M)]
my_combination(row_list,0,3,0)
