import heapq

test_list = [4, 3, 2, 5, 1]
print(test_list)

heapq.heapify(test_list)
print(test_list)
heapq.heappush(test_list,3.5)

for i in range(6):
    a = heapq.heappop(test_list)
    print(a)