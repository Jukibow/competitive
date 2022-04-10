from collections import deque


def main():
    # 入力
    Q = int(input())

    # # 山札
    # card_list = []

    # for num in range(Q):
    #     t, x = map(int, input().split())

    #     if t == 1:
    #         card_list.insert(0, x)
    #     elif t == 2:
    #         card_list.append(x)
    #     else:
    #         print(card_list[x-1])

    # 山札
    card_list = deque()

    for num in range(Q):
        t, x = map(int, input().split())

        if t == 1:
            card_list.appendleft(x)
        elif t == 2:
            card_list.append(x)
        else:
            print(card_list[x-1])


if __name__ == "__main__":
    main()
