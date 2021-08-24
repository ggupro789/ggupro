def my_combination(list, k, r, target):

    if len(target) == r:
        #탈출
        re = ''.join(target)
        return re

    if k >= len(list): #  k의 역활 이해
        return

    my_combination(list,k+1,r,target)
    my_combination(list,k+1,r,target+[list[k]])

def solution(orders, course):
    answer = []
    for number in course:
        result = {}
        for order in orders:
            x=''
            x = my_combination(list(map(str,order)),0,number,[])
            if x in result:
                result[x] += 1
            else:
                result[x] =1
        
        answer.append(k for k,v in result.items() if max(result.values()) == v) 
    
    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))
