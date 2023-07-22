# param
N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]
visited = [[False]*M for _ in range(N)]  # 訪問済みノードのマーキング用

dx = [1, 0, -1, 0]  # 右、下、左、上への移動に対応
dy = [0, 1, 0, -1]  # 右、下、左、上への移動に対応

def dfs(x, y):
    # 範囲外または訪問済み、あるいは岩の場合は何もしない
    if x < 0 or y < 0 or x >= N or y >= M or visited[x][y] or S[x][y] == '#':
        return
    visited[x][y] = True  # ノードを訪問済みにマーク
    for i in range(4):
        nx, ny = x, y
        while True:  # 岩にぶつかるまで移動
            nx += dx[i]
            ny += dy[i]
            if not(0 <= nx < N) or not(0 <= ny < M) or S[nx][ny] == '#':
                nx -= dx[i]
                ny -= dy[i]
                dfs(nx, ny)
                break  # 岩にぶつかったらその方向への移動を止める
            else:
                visited[nx][ny] = True

# 開始ノードでDFSを開始
dfs(2, 2)

# 訪問可能な氷のマスの数を求める
num_ice = sum(row.count(True) for row in visited)
print(num_ice)
