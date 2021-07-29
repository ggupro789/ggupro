# 1부터 12까지의 숫자를 원소로 가진 집합 A가 있다. 집합 A의 부분 집합 중 N개의 원소를 갖고 있고,
#  원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.
# 해당하는 부분집합이 없는 경우 0을 출력한다. 모든 부분 집합을 만들어 답을 찾아도 된다.
from itertools import combinations
test_case = int(input())
A = [i for i in range(1,13)]

for i in range(test_case):
    NK = list(map(int,input().split()))
    N_list = list(combinations(A,NK[0]))
    k_count = 0
    
    for k in N_list:
        if(sum(k) == NK[1]):
            k_count += 1

    print("#{0} {1}".format(i+1,k_count))