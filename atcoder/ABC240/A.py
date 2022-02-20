def main():

    a, b = input().split()

    if (int(b) - int(a)) == 1 or (int(b) - int(a)) == 9:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
