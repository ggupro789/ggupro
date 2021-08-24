def my_combination(list, k, r, target):
    global result
    if len(target) == r:
        #탈출
        re = ''.join(target)
        if re in result.keys():
          result[re] += 1
        else:
          result[re] = 1
        return

    if k >= len(list): #  k의 역활 이해
        return

    my_combination(list,k+1,r,target)
    my_combination(list,k+1,r,target+[list[k]])

def solution(orders, course):
    global result
    answers = []
    for number in course:
        result = {}
        for order in orders:
            my_combination(sorted(list(map(str,order))),0,number,[])
        if len(result.keys()) >= 2:
          x = [k for k,v in result.items() if max(result.values()) == v and v >= 2]
          for i in x:
            answers.append(i)

    answer = sorted(answers)
    return answer

result = {}