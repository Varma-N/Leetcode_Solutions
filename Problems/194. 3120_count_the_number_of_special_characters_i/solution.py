class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        seen = set(word)
        res = set()
        for i in seen:
            if i.upper() in seen and i.lower() in seen:
                res.add(i.lower())
        return len(res)
