
def main():
    # 入力
    N = int(input())

    A, B, C = map(int, input().split())
    max = 9999

    min_count = 9999

    for a in range(max):
        if a*A > N:
            break
        for b in range(max - a):
            if a*A + b*B > N:
                break
            if (N - (A*a + B*b)) % C == 0:
                count = a + b + ((N - (A*a + B*b)) // C)
                if count < min_count:
                    min_count = count

    print(min_count)


if __name__ == "__main__":
    main()
