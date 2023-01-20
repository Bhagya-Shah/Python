if __name__ == '__main__':
    n = int(input())
    arr = list(sorted(set(list(map(int, input().split())))))
    print(arr[-2])


