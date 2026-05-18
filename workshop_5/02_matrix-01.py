from typing import List
from collections import deque


def updateMatrix(mat: List[List[int]]) -> List[List[int]]:
    m = len(mat)
    n = len(mat[0])

    dist = [[float("inf")] * n for _ in range(m)]
    queue = deque()

    # Все нули - стартовые точки бфс
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                dist[i][j] = 0
                queue.append((i, j))

    directions = [
        (1, 0),   # вниз
        (-1, 0),  # вверх
        (0, 1),   # вправо
        (0, -1)   # влево
    ]

    while queue:
        r, c = queue.popleft()

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < m and 0 <= nc < n:
                if dist[nr][nc] > dist[r][c] + 1:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))

    return dist


def main():
    # 1
    mat = [[0,0,0],[0,1,0],[0,0,0]]
    assert updateMatrix(mat) == [[0,0,0],[0,1,0],[0,0,0]]

    # 2
    mat = [[0,0,0],[0,1,0],[1,1,1]]
    assert updateMatrix(mat) == [[0,0,0],[0,1,0],[1,2,1]]


if __name__ == "__main__":
    main()
