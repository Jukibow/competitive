class Count:
    result = []

    def get(self):
        return len(self.result)

    def add(self, val):
        self.result.append(val)


# 入力
N, M, K = map(int, input().split())


def main():

    current = 0
    depth = 0
    count = Count()
    calc(current, count, depth)

    print(count.get() % 998244353)


def calc(current, count, depth):

    for m in range(1, M+1):
        if current + m > K:
            break
        elif depth + 1 == N:
            count.add(current)
            break
        else:
            calc(current+m, count, depth+1)


if __name__ == '__main__':
    main()
