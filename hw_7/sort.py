def merge(lst1: list, lst2: list):
    result = []
    i, j = 0, 0

    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            result.append(lst1[i])
            i += 1
        else:
            result.append(lst2[j])
            j += 1
    while i < len(lst1):
        result.append(lst1[i])
        i += 1
    while j < len(lst2):
        result.append(lst2[j])
        j += 1
    
    return result

def mergeSort(lst: list) -> list:
    if len(lst) < 2: return lst

    mid = len(lst) // 2

    left, right = lst[:mid], lst[mid:]

    return merge(mergeSort(left), mergeSort(right))

def main():
    _ = int(input())
    print(*mergeSort(list(map(int, input().split()))))


if __name__ == "__main__":
    main()
