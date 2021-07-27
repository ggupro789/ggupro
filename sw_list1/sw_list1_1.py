# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.

test_case = int(input())


for i in range(test_case):
    N = int(input())
    result_list = list(map(int,input().split(' ')))

    if(N != len(result_list)):
        print("값을 제대로 넣어주세요")
        break
    
    print("#{0} {1}".format(i+1, max(result_list) - min(result_list) ))
