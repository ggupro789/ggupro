def solution(new_id:str):
    answer = ''
    
    answer = new_id.lower() # 1 단계
    answer_list = list(map(str,answer))
    
    
    second_discrimination = ['-','_','.'] # 2 단계
    cut = []
    for i in answer_list:
        if i.isalnum() == False:
            if i not in second_discrimination:
                cut.append(i)
    for i in cut:
        answer_list.remove(i)

    remove_overlap = []                   # 3 단계
    remove_overlap.append(answer_list[0])

    for i in range(1,len(answer_list)):
        if answer_list[i] == '.':  
            if answer_list[i-1] != answer_list[i]:
                remove_overlap.append(answer_list[i])
        else:
            remove_overlap.append(answer_list[i])

    if len(remove_overlap) > 0:
        if remove_overlap[0] == '.':
            del remove_overlap[0]
    if len(remove_overlap) > 0:
        if remove_overlap[-1] == '.':
            del remove_overlap[-1]

    if len(remove_overlap) == 0:  # 5 단계
        remove_overlap.append('a')
    
    if len(remove_overlap) >= 16 :      # 6 단계
        while len(remove_overlap) != 15: 
            del remove_overlap[-1]

        if remove_overlap[-1] == '.':
            del remove_overlap[-1]
            

    if len(remove_overlap) <= 2:        # 7 단계
        while len(remove_overlap) != 3:
            remove_overlap.append(remove_overlap[-1])

    answer = ''.join(remove_overlap)

    return answer


new_id = input()
result = solution(new_id)
print(result)