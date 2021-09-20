from itertools import combinations_with_replacement

n = int(input())
info = [2,1,1,1,0,0,0,0,0,0,0]
target = [10,9,8,7,6,5,4,3,2,1,0]
res = list(combinations_with_replacement(target, n))
info.reverse()
countL = 0
countA = 0
last = -1
result = []
min = 100000

for i in range(len(res)):
    map_list = [0,0,0,0,0,0,0,0,0,0,0]
    mini = float(100000)
    for j in range(n):
        map_list[res[i][j]] += 1

    for i in range(len(map_list)):
        if map_list[i] != 0:
            if map_list[i] > info[i]:
                countL += i
                if mini == 100000:
                    mini = i
            else:
                countA += i
    
    if countL > countA: 
        if min > mini:
            min = mini
            result = map_list

print(result)