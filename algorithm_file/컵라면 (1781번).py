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
noodle_list = []
index = 1
result = 0

for i in range(N):
    deadline,noodle = map(int,input().split())
    map_list.append((deadline,noodle,i))
    noodle_list.append((noodle))
print(map_list)
visited = [False for _ in range(N)]

heapq.heapify(noodle_list)



for i in range(N):
    a = heapq.heappop(noodle_list)
    print(a)

