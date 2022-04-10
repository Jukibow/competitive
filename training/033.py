def main():

    H, W = map(int, input().split())

    lamp = [[0 for i in range(W)] for j in range(H)]

    count = 0
    if H == 1 or W == 1:
        # コーナーケース
        count = max(H, W)
    else:
        for h in range(H):
            for w in range(W):
                if turn_on(lamp, h, w, H, W):
                    count += 1

    print(count)


def turn_on(lamp, h, w, H, W):

    if isNotNone(h-1, w-1, H, W):
        if is_lighting(lamp, h-1, w-1):
            return False

    if isNotNone(h-1, w, H, W):
        if is_lighting(lamp, h-1, w):
            return False

    if isNotNone(h-1, w+1, H, W):
        if is_lighting(lamp, h-1, w+1):
            return False

    if isNotNone(h, w+1, H, W):
        if is_lighting(lamp, h, w+1):
            return False

    if isNotNone(h+1, w+1, H, W):
        if is_lighting(lamp, h+1, w+1):
            return False

    if isNotNone(h+1, w, H, W):
        if is_lighting(lamp, h+1, w):
            return False

    if isNotNone(h+1, w-1, H, W):
        if is_lighting(lamp, h+1, w-1):
            return False

    if isNotNone(h, w-1, H, W):
        if is_lighting(lamp, h, w-1):
            return False

    lamp[h][w] = 1
    return True


def is_lighting(lamp, h, w):
    if lamp[h][w] == 1:
        return True
    else:
        return False


def isNotNone(h, w, H, W):

    if 0 <= h < H and 0 <= w < W:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
