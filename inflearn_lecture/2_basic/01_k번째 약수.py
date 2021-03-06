import sys
from examine import examine

@examine
def solution(*args):
    n, k = map(int, args[0][0].split())
    count, start = 0, 0
    while count != k:
        start += 1
        if start > n:
            return str(-1)
            break
        if n % start == 0:
            count += 1
    else:
        return str(start)

if __name__ == "__main__":
    solution()

else:
    input = sys.stdin.readline

    n, k = map(int, input().split())
    count, start = 0, 0

    while count != k:
        start += 1
        if start > n:
            print(-1)
            break
        if n % start == 0:
            count += 1
    else:
        print(start)