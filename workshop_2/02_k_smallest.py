def kSmallest(matrix: list[list[int]], k: int) -> int:
    if k == 1:
        return matrix[0][0]
    
    low, high = matrix[0][0], matrix[-1][-1]
    mid = low + (high - low) // 2

    while low <= high:
        count = 0
        row, col = len(matrix) - 1, 0

        while count < k:
            if row < 0 or col >= len(matrix[0]):
                break

            if matrix[row][col] <= mid:
                count += row + 1
                col += 1
            else:
                row -= 1
        
        if count < k:
            low = mid + 1
        else:
            high = mid - 1
        mid = low + (high - low) // 2
    
    return low

def main():
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    k = int(input())

    print(kSmallest(matrix, k))


if __name__ == "__main__":
    main()
