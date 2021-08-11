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
    visited_robot[0] = 1
    visited_robot[-1] = 0

    for belt in range(N-2,-1,-1):
        if visited_robot[belt] == 1 and visited_robot[belt+1] == 0 and deq[belt+1] != 0 :
            deq[belt+1] -= 1
            visited_robot[belt+1] = 1
            visited_robot[belt] = 0

    visited_robot.appendleft(visited_robot.pop())
    deq.appendleft(deq.pop())
    count = deq.count(0)
    howmany_count += 1
    if count  >= K:
        break

print(howmany_count)