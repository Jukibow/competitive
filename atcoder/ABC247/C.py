def main():
    # 入力
    N = int(input())

    print(*create(N))


def create(n):
    if n == 1:
        return [1]
    else:
        # 左側
        right = create(n-1)
        # 中央
        center = [n]
        # 右側
        left = create(n-1)

        return right + center + left


if __name__ == '__main__':
    main()
