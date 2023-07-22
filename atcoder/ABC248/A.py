
# 入力
S = input()


def main():
    S_list_old = list(S)
    S_list = [int(s) for s in S_list_old]

    result = [0]*10
    for s in S_list:
        result[s] = 1

    for index, item in enumerate(result):
        if item == 0:
            print(index)


if __name__ == "__main__":
    main()
