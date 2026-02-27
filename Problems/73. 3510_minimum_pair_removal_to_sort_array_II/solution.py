class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        # Doubly linked list
        prev = [-1] * n
        nxt = [-1] * n
        alive = [True] * n

        for i in range(n):
            if i > 0:
                prev[i] = i - 1
            if i < n - 1:
                nxt[i] = i + 1

        # Count inversions
        bad = 0
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                bad += 1

        if bad == 0:
            return 0

        # Min-heap of (sum, left_index)
        heap = []
        for i in range(n - 1):
            heapq.heappush(heap, (nums[i] + nums[i + 1], i))

        ops = 0

        while bad > 0:
            s, i = heapq.heappop(heap)

            # Validate pair
            j = nxt[i]
            if j == -1 or not alive[i] or not alive[j]:
                continue
            if nums[i] + nums[j] != s:
                continue

            # Remove old inversion contributions
            if prev[i] != -1 and nums[prev[i]] > nums[i]:
                bad -= 1
            if nums[i] > nums[j]:
                bad -= 1
            if nxt[j] != -1 and nums[j] > nums[nxt[j]]:
                bad -= 1

            # Merge
            nums[i] += nums[j]
            alive[j] = False
            nxt[i] = nxt[j]
            if nxt[j] != -1:
                prev[nxt[j]] = i

            # Add new inversion contributions
            if prev[i] != -1 and nums[prev[i]] > nums[i]:
                bad += 1
            if nxt[i] != -1 and nums[i] > nums[nxt[i]]:
                bad += 1

            # Push new adjacent sums
            if prev[i] != -1:
                heapq.heappush(heap, (nums[prev[i]] + nums[i], prev[i]))
            if nxt[i] != -1:
                heapq.heappush(heap, (nums[i] + nums[nxt[i]], i))

            ops += 1

        return ops
