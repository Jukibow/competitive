# 入力
A, B, K = map(int, input().split())


def main():

    a = A
    count = 0
    while True:
        if a >= B:
            break
        else:
            a = a*K
            count += 1

    print(count)


if __name__ == "__main__":
    main()
