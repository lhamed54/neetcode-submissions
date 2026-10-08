class Solution:
    def isValid(self, s: str) -> bool:
        
        # '{{[()([])]}}'

        #1. check if same num of brackets - done
        # split string into list of chars, count n. of brackets, if mod 2 == 0 then even


        #2. have to be in the same order
        # use stack ?
        

        brackets = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        stack = []
        for b in s:
            if not b in brackets:
                stack.append(b)
            else:
                if not stack or stack.pop() != brackets[b]:
                    return False
        return not stack


