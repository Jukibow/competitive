def main():

    # 入力
    N = int(input())

    A = list(map(int, input().split()))

    Q = int(input())

    B = [int(input()) for _ in range(Q)]

    # A を昇順にソート
    A.sort()

    # B に近いレートをひとつずつ二分岐探索
    # 自分より小さいレートを見つけて、+1のデータと絶対値比較

    for item in B:
        print(binary_search_find_closest(A, item))


def binary_search_find_closest(data, target):

    if len(data) == 0:
        return None
    if len(data) == 1:
        return abs(target - data[0])
    min_diff = float('inf')
    imin = 0
    imax = len(data) - 1
    closest_num = None
    while imin <= imax:
        imid = imin + (imax - imin) // 2
        #　中心の左右の値と目標との差を計算する。
        if imid + 1 < len(data):
            min_diff_right = abs(data[imid+1] - target)
        if imid > 0:
            min_diff_left = abs(data[imid-1] - target)
        # 最初の差と最も最小に近い値を更新する。
        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_num = data[imid-1]
        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_num = data[imid+1]
        # 2分探索する。
        if data[imid] < target:
            imin = imid + 1
        elif data[imid] > target:
            imax = imid - 1
        else:
            return abs(target - data[imid])
    return abs(target - closest_num)


if __name__ == "__main__":
    main()
