
def solve(mid):
    # 切った数のカウンタ
    counter = 0
    # 既に切った長さ
    cutLength = 0

    for i in A:
        i = int(i)
        if i - cutLength >= mid and L - i >= mid:
            cutLength = i
            counter += 1

    if counter >= K:
        return True
    else:
        return False


def main():

    input1 = input().split()

    global N
    N = int(input1[0])
    global L
    L = int(input1[1])

    global K
    K = int(input())

    input3 = input().split()

    global A
    A = input3

    left = -1
    right = L+1
    while(right - left > 1):
        mid = left + (right - left) // 2
        if solve(mid):
            left = mid
        else:
            right = mid

    print(left)


if __name__ == "__main__":
    main()
