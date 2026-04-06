def binarySearch(N: int, lst: list, target: int) -> int:

    left, right = 0, N - 1
    middle = (left + right) // 2

    while left <= right:
        if target == lst[middle]:
            return middle
        elif target < lst[middle]:
            right = middle - 1
        else:
            left = middle + 1
        
        middle = (left + right) // 2
    
    return middle + 1

def main():
    print(binarySearch(
        N = int(input()),
        lst = list(map(int, input().split())),
        target = int(input())
    ))


if __name__ == "__main__":
    main()
