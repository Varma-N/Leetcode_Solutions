class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = Counter(word)
        sorted_counts = sorted(counts.values(), reverse=True)
        
        total_pushes = 0
        for i, count in enumerate(sorted_counts):
            total_pushes += count * ((i // 8) + 1)
            
        return total_pushes