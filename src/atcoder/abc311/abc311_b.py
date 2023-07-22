# param
N, D = map(int, input().split())
#空のリスト
S = []
for _ in range(N):
    S.append(input())

# solve
result = 0
result_tmp = 0
for d in range(D):
    for n in range(N):
        if S[n][d] == "x":
            result_tmp = 0
            break
    else:
        result_tmp += 1
        result = max(result, result_tmp)

print(result)
