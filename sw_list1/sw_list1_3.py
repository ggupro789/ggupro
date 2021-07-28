#sw_list1_8차시 문제

test_case = int(input())

for i in range(test_case):
    N = int(input())
    number = input() 
    number_list = list(map(int,number)) # 숫자 한 개 씩 리스트로
    number_list.sort(reverse=True) #카운트 같을 때 높은 숫자 출력되도록
    
    new_count = {} # key= 숫자 , value = 카운트 되는 dictionary

    for j in number_list: 
        try:
            new_count[j] += 1
        except KeyError:  # new_count에 number_list 숫자 없으면 그 키값에 1로 시작
            new_count[j] = 1

    max_key = max(new_count,key=new_count.get)  # value 기준 max 값 가지는 key 값 참조.

    print("#{0} {1} {2}".format(i+1,max_key,new_count[max_key]))
