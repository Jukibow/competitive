# param
N = int(input())
A = [0] + list(map(int, input().split()))

visited = [False]*(N+1)
order = []  # 訪れた頂点の順番を保持
node = 1  # スタートノード

while not visited[node]:
    visited[node] = True
    order.append(node)
    node = A[node]

cycle_start = order.index(node)  # 閉路が始まるノードのインデックス
cycle = order[cycle_start:]  # 閉路部分の頂点のリスト

print(len(cycle))
print(" ".join(map(str, cycle)))
