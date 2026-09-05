from scipy.stats import rankdata
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        return rankdata(arr, method='dense').tolist()
        
        


