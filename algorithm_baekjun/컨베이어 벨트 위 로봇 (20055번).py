import collections

N,K = map(int,input().split())

visited_robot = collections.deque()
for _ in range(N):
    visited_robot.append(0)

durability = list(map(int,input().split()))
deq = collections.deque()

for A in durability:
    deq.append(A)

count = 0
howmany_count = 0

while True:

    visited_robot.appendleft(visited_robot.pop())  # 1 단계
    deq.appendleft(deq.pop())
    visited_robot[-1] = 0

    for belt in range(N-2,-1,-1):
        if visited_robot[belt] == 1 and visited_robot[belt+1] == 0 and deq[belt+1] >= 1 :  # 2 단계
            deq[belt+1] -= 1
            visited_robot[belt+1] = 1
            visited_robot[belt] = 0
    visited_robot[N-1] = 0

    if deq[0] >= 1 and visited_robot[0] == 0:  # 3 단계
        visited_robot[0] = 1
        deq[0] -= 1


    count = deq.count(0)  # 4 단계
    howmany_count += 1
    if count  >= K:
        break
    
print(howmany_count)