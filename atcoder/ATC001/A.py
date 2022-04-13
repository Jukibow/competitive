import sys

sys.setrecursionlimit(1000000)

H, W = map(int, input().split())

c = [list(input()) for l in range(H)]

visited = [[0]*W for _ in range(H)]


def main():

    # スタート位置を取得
    h_start, w_start = get_start()

    # ゴールを探す
    # 深さ優先探索
    dfs(h_start, w_start)

    print('No')


def get_start():
    # スタート位置を返却
    for w in range(W):
        for h in range(H):
            if c[h][w] == 's':
                return h, w


def dfs(h, w):
    if visited[h][w] == 1:
        return
    visited[h][w] = 1
    # 深さ優先探索
    if c[h][w] == 'g':
        print("Yes")
        sys.exit()

    if c[h][w] == '#':
        return

    # 上
    if h - 1 >= 0:
        dfs(h - 1, w)

    # 右
    if w + 1 < W:
        dfs(h, w + 1)

    # 下
    if h + 1 < H:
        dfs(h + 1, w)

    # 左
    if w - 1 >= 0:
        dfs(h, w - 1)


if __name__ == "__main__":
    main()
