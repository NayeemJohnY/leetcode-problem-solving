class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # ch_list = []
        # valid = True
        # for ch in s:
        #     if ch in ['(', '{', '[']:
        #         ch_list.append(ch)
        #     else:
        #         if not ch_list:
        #             valid = False
        #             break
        #         if ch == ']':
        #             if ch_list.pop() != '[':
        #                 valid = False
        #                 break
        #         elif ch == '}':
        #             if ch_list.pop() != '{':
        #                 valid = False
        #                 break
        #         elif ch == ')':
        #             if ch_list.pop() != '(':
        #                 valid = False
        #                 break
        # if valid:
        #     valid = not ch_list
        # return valid

        # Solution 2
        ch_list = []
        mappings = {')': '(', '}': '{', ']': '['}
        for ch in s:
            if ch in mappings.values():
                ch_list.append(ch)
            elif not ch_list or ch_list.pop() != mappings[ch]:
                return False
        return not ch_list


solution = Solution()
print(solution.isValid("([)]"))
print(solution.isValid("[{()}]"))
print(solution.isValid("([]"))

# ([)] - all though balanced but not valid
# ([] - not valid due to unbalanced
# stack
# starts with closure then invalid )}]
# ends with open then invalid ([{
# [{()}]

# ]
# (
# { -
# [ - pop
