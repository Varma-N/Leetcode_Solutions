class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        if '{' not in expression:
            return [expression]
        
        right = expression.find('}')
        left = expression.rfind('{', 0, right)
        parts = expression[left+1:right].split(',')
        
        res = set()
        for p in parts:
            res.update(self.braceExpansionII(expression[:left] + p + expression[right+1:]))
        return sorted(list(res))