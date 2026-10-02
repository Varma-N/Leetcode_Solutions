class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        m, n = len(word1), len(word2)
        suf = [0] * (m + 1)
        j = n - 1
        
        # Precompute suffix match lengths
        for i in range(m - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                j -= 1
            suf[i] = n - 1 - j

        seq = []
        changed = False
        i = 0
        
        # Greedily pick indices
        for k in range(n):
            while i < m:
                if word1[i] == word2[k]:
                    if changed:
                        # If a change was already used, we MUST be able to finish exactly
                        if suf[i + 1] >= n - k - 1:
                            seq.append(i)
                            i += 1
                            break
                    else:
                        # If a change hasn't been used, greedily taking the exact match is always optimal
                        seq.append(i)
                        i += 1
                        break
                else:
                    # If they don't match, we can use our 1 allowed change ONLY IF it guarantees an exact finish
                    if not changed and suf[i + 1] >= n - k - 1:
                        seq.append(i)
                        changed = True
                        i += 1
                        break
                i += 1
            else:
                # If the while loop exhausted `i` without breaking, we cannot complete the sequence
                return []
                
        return seq if len(seq) == n else []