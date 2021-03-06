from examine import examine
import sys

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')

    N = int(input())
    res = [0] * N
    target = []
    for i in range(N):
        target.append([int(num) for num in input().split()])

    target.sort(key=lambda x:x[0], reverse=True)

    for i in range(N):
        MAX = 0
        for j in range(i):
            if target[i][-1] < target[j][-1]:
                MAX = max(res[j], MAX)
        res[i] = MAX + target[i][1]
        # 반복문 안의 다른 코드 다 지우고 아래 한 줄로 처리할 수도 있음.
        # res[i] = max([res[j] if target[i][-1] < target[j][-1] else 0 for j in range(i + 1)]) + target[i][1]

    return [str(max(res))]

if __name__ == "__main__":
    print(solution(examine=True))
