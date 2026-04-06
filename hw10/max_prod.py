N = int(input())
lst = list(map(int, input().split()))
K = int(input())

max_dp = [None] * (K + 1)
min_dp = [None] * (K + 1)

max_dp[0] = 1
min_dp[0] = 1

for x in lst:
    for k in range(K, 0, -1):
        candidates = []

        if max_dp[k - 1] is not None:
            candidates.append(max_dp[k - 1] * x)
        if min_dp[k - 1] is not None:
            candidates.append(min_dp[k - 1] * x)
        
        if not candidates:
            continue

        cur_max = max(candidates)
        cur_min = min(candidates)

        if max_dp[k] is None or cur_max > max_dp[k]:
            max_dp[k] = cur_max
        if min_dp[k] is None or cur_min < min_dp[k]:
            min_dp[k] = cur_min

print(max_dp[K])
