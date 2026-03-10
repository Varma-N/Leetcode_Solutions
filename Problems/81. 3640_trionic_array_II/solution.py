from collections import deque
from typing import List

class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]
        
        left_inc = [0] * n
        left_inc[0] = 0
        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                left_inc[i] = left_inc[i - 1]
            else:
                left_inc[i] = i
        
        right_inc = [0] * n
        right_inc[n - 1] = n - 1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                right_inc[i] = right_inc[i + 1]
            else:
                right_inc[i] = i
        
        left_dec = [0] * n
        left_dec[0] = 0
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                left_dec[i] = left_dec[i - 1]
            else:
                left_dec[i] = i
        
        INF = 10**30
        NEG_INF = -10**30
        
        m_arr = [INF] * n
        dq_left = deque()
        for i in range(n):
            if i > 0:
                while dq_left and pref[dq_left[-1]] >= pref[i - 1]:
                    dq_left.pop()
                dq_left.append(i - 1)
            L_bound = left_inc[i]
            if L_bound < i:
                while dq_left and dq_left[0] < L_bound:
                    dq_left.popleft()
                m_arr[i] = pref[dq_left[0]]
        
        N = n + 1
        LOG = (N).bit_length()
        st_table = [[0] * N for _ in range(LOG)]
        for i in range(N):
            st_table[0][i] = pref[i]
        
        for k in range(1, LOG):
            step = 1 << (k - 1)
            for i in range(N - (1 << k) + 1):
                st_table[k][i] = max(st_table[k - 1][i], st_table[k - 1][i + step])
        
        def query_max(l, r):
            if l > r:
                return NEG_INF
            length = r - l + 1
            k = length.bit_length() - 1
            return max(st_table[k][l], st_table[k][r - (1 << k) + 1])
        
        M_arr = [NEG_INF] * n
        for i in range(n):
            if right_inc[i] > i:
                l_idx = i + 2
                r_idx = right_inc[i] + 1
                M_arr[i] = query_max(l_idx, r_idx)
        
        dq_peaks = deque()
        ans = NEG_INF
        for q in range(n):
            Ld = left_dec[q]
            while dq_peaks and dq_peaks[0] < Ld:
                dq_peaks.popleft()
            if M_arr[q] != NEG_INF and dq_peaks:
                current_sum = M_arr[q] - m_arr[dq_peaks[0]]
                if current_sum > ans:
                    ans = current_sum
            if m_arr[q] != INF:
                while dq_peaks and m_arr[dq_peaks[-1]] >= m_arr[q]:
                    dq_peaks.pop()
                dq_peaks.append(q)
        
        return ans
