#sw_list1_9차시 문제

test_case = int(input())

for i in range(test_case):
    x = list(map(int,input().split(' ')))
    number_list = map(int,input().split(' '))
    maxmin = []
 
    for k in range(len(number_list)-x[1]+1): # 전체 배열 - 묶는배열 크기 해서 indexerror 방지
        sum = 0
        for j in range(k,k+x[1]): # 묶는 배열 크기만큼 더하기

            sum += number_list[j]
            
        maxmin.append(sum)
    print("#{0} {1}".format(i+1,max(maxmin)-min(maxmin)))

        


    

         