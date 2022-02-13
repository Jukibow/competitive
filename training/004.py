import numpy as np


def main():

    H, W = map(int, input().split())

    A = [list(map(int, input().split())) for l in range(H)]

    np_A = np.array(A)

    # 列の合計
    col_sum = np.sum(np_A, axis=0)
    # 行の合計
    row_sum = np.sum(np_A, axis=1)

    # 結果格納用
    result = [[0] * W for i in range(H)]

    # 計算
    for h in range(H):
        for w in range(W):
            result[h][w] = col_sum[w] + row_sum[h] - A[h][w]
            print(str(result[h][w]) + " ", end="")
        print()


if __name__ == "__main__":
    main()
