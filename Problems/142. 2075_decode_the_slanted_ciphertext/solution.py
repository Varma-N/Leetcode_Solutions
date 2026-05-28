class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if not encodedText or rows == 1:
            return encodedText
        cols = len(encodedText) // rows
        res = []

        for i in range(cols):
            current_row, current_col = 0, i

            while current_row < rows and current_col < cols:
                index = current_row * cols + current_col
                res.append(encodedText[index])
                current_col += 1
                current_row += 1
        return ''.join(res).rstrip()
                



