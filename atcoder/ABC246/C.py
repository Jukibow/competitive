def main():
    # 入力
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))

    count = 0
    amount = 0
    # 1. 0円以上になるように値下げ
    for index, a in enumerate(A):
        used = a // X
        if count + used <= K:
            # まだクーポンが余ってる場合
            # ちょうどクーポンを使い切った場合
            count += used
            A[index] = a - used * X
            amount += A[index]
        else:
            # クーポンが超過した場合
            # 使える枚数だけ使う
            count += K - count
            amount += a - (K - count) * X

    # 2. 0円以下になるように値下げ
    # 降順にソート
    if K - count > 0:
        A.sort(reverse=True)
        for i in range(K - count):
            if i+1 > N:
                break
            amount -= A[i]

    print(amount)


if __name__ == '__main__':
    main()
