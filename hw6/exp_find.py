def exp_find(N: int, lst: list, target: int) -> tuple:
    border = 1
    lastEl = len(lst) - 1

    while border < lastEl and lst[border] <= target:
        if lst[border] == target:
            return (border, border + 1)
        
        border *= 2
    
    return (border // 2, border)


def main():
    l, r = exp_find(
        int(input()),
        list(map(int, input().split())),
        int(input())
    )
    print(l, r)

if __name__ == "__main__":
    main()
