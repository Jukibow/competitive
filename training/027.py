
def main():

    # 入力
    N = int(input())

    # result_item = []
    # for index in range(N):
    #     item = input()
    #     if item not in result_item:
    #         result_item.append(item)
    #         print(index+1)

    mydict = {}
    for n in range(N):
        item = input()
        if item not in mydict:
            mydict[item] = n + 1
            print(n + 1)


if __name__ == '__main__':

    main()
