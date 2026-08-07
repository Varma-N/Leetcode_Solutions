class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        input_map = dict()
        res = []
        for i in range(26):
            input_map[chr(97+i)] = weights[i]
        for word in words:
            word_weight = 0
            for char in word:
                word_weight += input_map[char] 
            word_weight %= 26
            res.append(chr(122-word_weight))
        return ''.join(res)


        