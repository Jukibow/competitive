def main():

    # 入力
    N, M = map(int, input().split())

    graph = [[] for i in range(N)]
    for m in range(M):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    count = 0
    for i in range(N):
        count_i = 0
        for item in graph[i]:
            if item < i:
                count_i += 1

        if count_i == 1:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
