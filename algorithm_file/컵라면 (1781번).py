import heapq

# test_list = [4, 3, 2, 5, 1]
# print(test_list)

# heapq.heapify(test_list)
# print(test_list)
# # heapq.heappush(test_list,3.5)

# for i in range(5):
#     a = heapq.heappop(test_list)
#     print(a)

N = int(input())
map_list = []
for i in range(1,N+1):
    deadline,noodle = map(int,input().split())
    map_list.append((deadline,noodle,i))

print(map_list)
visited = [False for _ in range(N)]
print("---------")
heapq.heapify(map_list)

for i in range(N):
    dd,bb,cc = heapq.heappop(map_list)
    print(dd,bb,cc)
    
