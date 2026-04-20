def max_length(st: str) -> int:
    if len(st) < 2:
        return len(st)

    letters = set()
    cur_len, max_len = 1, 0

    letters.add(st[0])
    left, right = 0, 1
    while right < len(st):
        x = st[right]

        while x in letters:
            letters.remove(st[left])
            left += 1
            cur_len -= 1
        
        letters.add(x)
        cur_len += 1
        max_len = max(max_len, cur_len)
        right += 1
    
    return max_len

def main():
    print(max_length(input()))


if __name__ == "__main__":
    main()
