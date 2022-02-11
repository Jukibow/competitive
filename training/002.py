
def check(kakko):

    height = 0

    for j in list(kakko):
        if j == '(':
            height += 1
        else:
            height += -1

        if height < 0:
            return False

    if height == 0:
        return True
    else:
        return False


def main():

    # 入力
    global N
    N = int(input())

    # 2進数で0 → 2^N - 1までループ
    # 1から始まる→")"から始まる場合は正しくないため、後半は計算しない
    for num in range((2 ** N)//2):

        num_bit = format(num,  'b').zfill(N)

        num_bit_list = list(num_bit)
        kakko = ''

        for i in num_bit_list:
            if i == '0':
                kakko += '('
            else:
                kakko += ')'

        if check(kakko):
            print(kakko)


if __name__ == "__main__":
    main()
