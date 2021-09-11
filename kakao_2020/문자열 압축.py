def solution(s):
    answer = 0
    list_basic = s[0:len(s):1]  # s 문자열 문자 하나씩
    maxi = 1          # 문자열 나눌 수
    count_list = []   # 나눴을 때 문자열 길이 담을 리스트
    
    while maxi <= int(len(s)/2) :   # 홀수 일땐 홀수/2 -1 짝수일땐 짝수/2 까지 범위
        total_list = ''      # 나눴을 때 만들어지는 리스트
         # 중간에서 계속 판별해줄 리스트
        count = 0      #

        for i in range(0,len(list_basic)-maxi,maxi):
            if i == 0:
                middle_list = list_basic[i:i+maxi]

            word_list = list_basic[i:i+maxi]

            if middle_list == word_list:
                count += 1
                total_list = total_list+word_list

            elif middle_list != word_list:
                middle_list = list_basic[i:i+maxi]
                if count != 0:
                    total_list = total_list+str(count)+word_list
                else: 
                    total_list = total_list + word_list

                count = 1

        count_list.append(len(total_list))
        maxi += 1
        print(total_list)
        
        

    return min(count_list)


s = input()
print(solution(s))
