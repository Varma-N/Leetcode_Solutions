class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        knowledge_dict = dict(knowledge)
        result = []
        current_key = ""
        inside_bracket = False
        for i in range(len(s)):
            if s[i] == '(':
                inside_bracket = True
            elif s[i] == ')':
                inside_bracket = False
                result.append(knowledge_dict.get(current_key, "?"))
                current_key = ""
            elif inside_bracket:
                current_key += s[i]
            else:
                result.append(s[i])
        return "".join(result)