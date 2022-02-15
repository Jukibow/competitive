from functools import reduce
import math


def my_gcd(*numbers):
    '''
    最大公約数
    '''
    return reduce(math.gcd, numbers)


def main():
    # 入力
    A, B, C = input().split()

    # 最大公約数を求める
    gcd = my_gcd(int(A), int(B), int(C))

    result = (int(int(A)//gcd) - 1) + \
        (int(int(B)//gcd) - 1) + (int(int(C)//gcd) - 1)
    print(int(result))


if __name__ == "__main__":
    main()
