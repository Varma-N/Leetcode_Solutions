class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        
        # Penalty if shop closes at hour 0
        penalty = customers.count('Y')
        min_penalty = penalty
        best_hour = 0

        for j in range(n):
            if customers[j] == 'Y':
                penalty -= 1  # customer is now served
            else:
                penalty += 1  # shop stayed open unnecessarily

            if penalty < min_penalty:
                min_penalty = penalty
                best_hour = j + 1

        return best_hour
