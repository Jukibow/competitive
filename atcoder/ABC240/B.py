def main():

    N = int(input())
    A = input().split()

    count = 0
    list = []
    for a in A:
        if int(a) in list:
            continue
        else:
            list.append(int(a))
            count += 1

    print(count)


if __name__ == "__main__":
    main()
