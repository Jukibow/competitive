
def main():
    '''
    TLEするのでボツ
    '''
    # 入力
    N = int(input())

    class_num = [0] * N
    point = [0] * N
    for i in range(N):
        A = input().split()
        class_num[i] = int(A[0])
        point[i] = int(A[1])

    Q = int(input())

    result1 = [0] * Q
    result2 = [0] * Q
    for q in range(Q):
        input_ = input().split()
        input1 = int(input_[0])
        input2 = int(input_[1])

        for i in range(input1-1, input2):
            if class_num[i] == 1:
                result1[q] += point[i]
            else:
                result2[q] += point[i]

    for q in range(Q):
        print(str(result1[q]) + " " + str(result2[q]))


def solve():
    # 入力
    N = int(input())

    result1 = [0] * (N+1)
    result2 = [0] * (N+1)
    sum1 = 0
    sum2 = 0
    for i in range(1, N+1):
        A = input().split()
        if int(A[0]) == 1:
            sum1 += int(A[1])
            result1[i] = sum1
            result2[i] = sum2
        else:
            sum2 += int(A[1])
            result1[i] = sum1
            result2[i] = sum2

    Q = int(input())
    result1_ = [0] * Q
    result2_ = [0] * Q
    for q in range(Q):
        input_ = input().split()
        input1 = int(input_[0])
        input2 = int(input_[1])

        result1_[q] = result1[input2] - result1[input1-1]
        result2_[q] = result2[input2] - result2[input1-1]

    for q in range(Q):
        print(str(result1_[q]) + " " + str(result2_[q]))


if __name__ == "__main__":
    solve()
