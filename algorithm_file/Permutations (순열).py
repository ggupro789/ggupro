# import itertools
# for item in itertools.permutations(temp_list,4):
#     print(item)

def my_permutations(list,r,target):
    #탈출조건
    if len(target) == r:
        # 결과를 수행하라
        print(target)
        return

    for i in range(len(list)):
        if visited[i] == False:
            visited[i] = True
            my_permutations(list,r,target+[list[i]])
            visited[i] = False # false로 다시 바꿔줘야 한다.

temp_list = [0,1,2,3,4,5]
visited = [False for _ in range(len(temp_list))]