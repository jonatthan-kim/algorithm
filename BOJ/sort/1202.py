# 210623 보석 도둑 gold2

import sys
from heapq import heappush, heappop
input = sys.stdin.readline
N, K = list(map(int, input().split()))  # N: 보석의 개수, K: 가방의 개수
jewelry, bag, pq, result, i = [], [0] * K, [], 0, 0

for _ in range(N):
    jewelry.append(list(map(int, input().split())))

jewelry.sort()

for j in range(K):
    bag[j] = int(input().strip())

bag.sort()

for b in bag:
    while i < N and b >= jewelry[i][0]:
        heappush(pq, -jewelry[i][1])
        i += 1

    if pq:
        result += -heappop(pq)
# for _ in range(N):
#     V, M = heappop(jewelry)
#     for i, c in enumerate(bag):
#         if M <= c:
#             bag[i] = 0
#             result += -V
#             K -= 1
#             break
#     if not K:
#         break

print(result)

# 내가 생각한 해법1
## 보석을 가치 순으로 정렬하고, 넣을 수 있는 가장 큰 가방에 먼저 집어넣기 시작
## 반례: 1 - 10, 2 - 9, 가방 무게: 1, 2

# 내가 생각한 해법2
## 보석을 가치 순으로 정렬하고, 넣을 수 있는 가장 작같 가방에 먼저 집어넣기 시작,
## 문제: O(N*K)의 시간이 걸림. 선형 시간 알고리즘을 찾는 것이 필요.
