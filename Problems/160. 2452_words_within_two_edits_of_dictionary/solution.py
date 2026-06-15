class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def get_dis(s1, s2):
            diff = 0
            for q, d in zip(s1, s2):
                if q != d:
                    diff += 1
                if diff > 2:
                    return False
            return True
        
        result = []
        for query in queries:
            for word in dictionary:
                if get_dis(query, word): 
                    result.append(query)
                    break
        return result


                

        