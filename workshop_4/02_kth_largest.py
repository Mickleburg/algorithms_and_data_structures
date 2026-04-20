import heapq

def findKthLargest(nums: list[int], k: int) -> int:
    heap = nums[:k]
    heapq.heapify(heap)

    for i in range(k, len(nums)):
        if nums[i] > heap[0]:
            heapq.heapreplace(heap, nums[i])
    
    return heap[0]


def main():
    print(findKthLargest(nums=[3,2,1,5,6,4], k=2))
    print(findKthLargest(nums=[3,2,3,1,2,4,5,5,6], k=4))


if __name__ == "__main__":
    main()
