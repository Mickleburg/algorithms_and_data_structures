from typing import List


def lengthOfLIS(nums: List[int]) -> int:
    n = len(nums)

    # dp[i] = длина самой длинной возрастающей подпоследовательности, которая заканчивается именно на nums[i]
    dp = [1] * n

    answer = 1

    for i in range(n):
        for j in range(i):
            # если nums[j] меньше nums[i], занчит nums[i] можно поставить после nums[j]
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

        answer = max(answer, dp[i])

    return answer


def main():
    # 1
    nums = [10,9,2,5,3,7,101,18]
    assert lengthOfLIS(nums) == 4

    # 2
    nums = [0,1,0,3,2,3]
    assert lengthOfLIS(nums) == 4

    # 3
    nums = [7,7,7,7,7,7,7]
    assert lengthOfLIS(nums) == 1


if __name__ == "__main__":
    main()
