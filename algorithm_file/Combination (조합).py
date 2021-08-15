# import itertools
# for item in itertools.combinations(temp_list,4):
#     print(item)

def my_combination(list, k, r, target):
    if len(target) == r:
        #탈출
        print(target)
        return

    if k >= len(list): #  k의 역활 이해
        return

    my_combination(list,k+1,r,target)
    my_combination(list,k+1,r,target+[list[k]])