# 바이러스 2606번
import collections
def bfs(relation):
    deq = collections.deque()
    deq.append(1)

    visited = [1]

    count = 0

    while len(deq) > 0:
        now = deq.popleft()

        for list in relation:
            if now in list:
                for computer in list:
                    if computer not in visited:
                        visited.append(computer)
                        deq.append(computer)
                        count += 1

    return count


computers = int(input())
relation_N = int(input())

relation = [list(map(int,input().split())) for _ in range(relation_N)]

print(bfs(relation))
