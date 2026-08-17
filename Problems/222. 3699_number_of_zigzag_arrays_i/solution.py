class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        # If the length is 1, any number in the range is valid.
        if n == 1:
            return r - l + 1
            
        MOD = 10**9 + 7
        
        # Step 1: Normalize the range. 
        # K represents the total number of available distinct integers.
        K = r - l + 1
        
        # Step 2: Initialize our DP state for length 1.
        # dp[v][0] = valid sequences ending in 'v' where the NEXT move must be DOWN.
        # dp[v][1] = valid sequences ending in 'v' where the NEXT move must be UP.
        # We use size K + 1 so we can 1-index the values for easier reading.
        dp = [[1, 1] for _ in range(K + 1)]
        dp[0] = [0, 0] 
        
        # Step 3 & 4: Build the sequence step-by-step up to length 'n'
        for length in range(2, n + 1):
            new_dp = [[0, 0] for _ in range(K + 1)]
            
            # Calculate transitions going UP.
            # If we are going UP to 'v', the previous number was smaller.
            # We need the sum of all valid paths ending in a smaller number 
            # that are ready to go UP (meaning their last move was DOWN).
            sum_down = 0
            for v in range(1, K + 1):
                new_dp[v][0] = sum_down
                # Add the current v's paths to our running sum for the next iteration
                sum_down = (sum_down + dp[v][1]) % MOD
                
            # Calculate transitions going DOWN.
            # If we are going DOWN to 'v', the previous number was larger.
            # We need the sum of all valid paths ending in a larger number 
            # that are ready to go DOWN (meaning their last move was UP).
            sum_up = 0
            for v in range(K, 0, -1):
                new_dp[v][1] = sum_up
                # Add the current v's paths to our running sum for the next iteration
                sum_up = (sum_up + dp[v][0]) % MOD
                
            # Move to the next length
            dp = new_dp
            
        # Step 5: Sum up all valid arrays of length 'n'
        total_valid_arrays = 0
        for v in range(1, K + 1):
            total_valid_arrays = (total_valid_arrays + dp[v][0] + dp[v][1]) % MOD
            
        return total_valid_arrays