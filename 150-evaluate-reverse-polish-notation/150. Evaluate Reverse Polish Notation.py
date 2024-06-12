class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # as the polish notation is always using the appeared 2 nums for the operated
        # using a stack to get the num for calculating
        # once finished the calculation push it back to the stack
        # each push pop is O(1)
        # time: O(N) space: O(N) for the stack
        def cal(num1, num2, oper):
            if oper == '+':
                return num1+num2
            elif oper == '-':
                return num1-num2
            elif oper == '*':
                return num1*num2
            return int(num1/num2)
        nums = []
        for tok in tokens:
            if tok in ['+', '-', '*', '/']:
                # do operation
                num2 = nums.pop()
                num1 = nums.pop()
                newNum = cal(num1, num2, tok)
                nums.append(newNum)
                # print(num1, num2, tok, newNum)
            else:
                nums.append(int(tok))
        return nums.pop()

        