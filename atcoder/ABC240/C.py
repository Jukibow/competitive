def main():

    # 入力
    global N, X
    N, X = input().split()
    N = int(N)
    X = int(X)

    ab = [map(int, input().split()) for _ in range(N)]
    global a, b
    a, b = [list(i) for i in zip(*ab)]

    sum = 0
    count = 0

    answer()


def solve(sum, count):
    ''' ボツ '''
    if sum == X and count == N:
        return True
    elif count == N or sum > X:
        return False
    else:
        sum_a = sum + a[count]
        sum_b = sum + b[count]
        count += 1

        return solve(sum_a, count) or solve(sum_b, count)


def answer():
    result = [[0] * (X+1) for n in range(N+1)]
    result[0][0] = 1
    for n in range(N):
        for x in range(X):
            if result[n][x] == 1:
                if x + a[n] <= X:
                    result[n + 1][x + a[n]] = 1
                if x + b[n] <= X:
                    result[n + 1][x + b[n]] = 1

    if result[N][X] == 1:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
