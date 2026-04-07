class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
        for h in range(12):
            for m in range(60):
                h_bits = bin(h).count('1')
                m_bits = bin(m).count('1')
                if h_bits + m_bits == turnedOn:
                    result.append(f'{h}:{m:02}')
        return result
