def main():
    # 入力
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    count = 0
    for i in range(len(A)):
        if A[i] > B[i]:
            count += A[i] - B[i]
            A[i] = B[i]
            if count > K:
                print('No')
                return
        elif A[i] < B[i]:
            count += B[i] - A[i]
            A[i] = B[i]
            if count > K:
                print('No')
                return

    if (K - count) % 2 == 0:
        print('Yes')
        return
    else:
        print('No')
        return


if __name__ == "__main__":

    main()
