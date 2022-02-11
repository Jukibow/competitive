import sys

sys.setrecursionlimit(200000)


def main():

    N = int(input())

    # 初期化
    first_diagram = [[0]*N for i in range(N)]
    second_diagram = [[0]*N for i in range(N)]
    # 経路を登録
    for n in range(N - 1):
        A, B = input().split()
        A, B = int(A), int(B)
        first_diagram[A-1][B-1] = 1
        first_diagram[B-1][A-1] = 1
        second_diagram[A-1][B-1] = 1
        second_diagram[B-1][A-1] = 1

    u = 0
    v = 0

    _, u = dfs(first_diagram, u, 0, u, 0)
    max, _ = dfs(second_diagram, u, 0, v, 0)
    print(max+1)

# 深さ優先探索


def dfs(diagram, current, depth, end, max_depth):

    for a in range(len(diagram[current])):
        if diagram[current][a] == 1:
            diagram[current][a] = 0
            diagram[a][current] = 0
            next_depth = depth + 1
            if next_depth > max_depth:
                max_depth = next_depth
                end = a
            max_depth, end = bft(diagram, a, next_depth, end, max_depth)
    return max_depth, end


if __name__ == "__main__":
    main()
