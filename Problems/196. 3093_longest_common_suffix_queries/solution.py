class TrieNode:
    def __init__(self):
        self.children = {}
        self.best_idx = -1

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        root = TrieNode()
        best_global_idx = 0
        
        for i in range(1, len(wordsContainer)):
            if len(wordsContainer[i]) < len(wordsContainer[best_global_idx]):
                best_global_idx = i
        
        root.best_idx = best_global_idx
        
        for i, w in enumerate(wordsContainer):
            node = root
            for char in reversed(w):
                if char not in node.children:
                    node.children[char] = TrieNode()
                    node.children[char].best_idx = i
                else:
                    curr_best = node.children[char].best_idx
                    if len(w) < len(wordsContainer[curr_best]):
                        node.children[char].best_idx = i
                node = node.children[char]
                
        ans = []
        for q in wordsQuery:
            node = root
            for char in reversed(q):
                if char in node.children:
                    node = node.children[char]
                else:
                    break
            ans.append(node.best_idx)
            
        return ans