import operator
import math
from numbers import Number

class OperatorError(Exception):
    pass

class OperandError(Exception):
    pass

class BracketsSeqError(Exception):
    pass

class ExpressionError(Exception):
    pass

class Calculator():    
    # Operation prefix/infix/postfix type
    PREFIX_OP = 0
    INFIX_OP = 1
    POSTFIX_OP = 2

    # Operation unary/binary type
    UNARY_OP = 0
    BIN_OP = 1

    # Supported operations
    SPACE_CONST = {' ', '\t', '\n'}
    MATH_CONST = {
        'pi':       math.pi,
    }

    BRACKETS_MAP = {'(': ')', '[': ']', '{': '}'}
    OPENING_BRACKETS = BRACKETS_MAP.keys()
    CLOSING_BRACKETS = BRACKETS_MAP.values()
    BRACKETS = OPENING_BRACKETS | CLOSING_BRACKETS

    # Operation: (prefix operation, infix operation)
    DUALISTIC_OPERATIONS = {'-': ('-#', '-')}
    STANDART_OPERATIONS = {'^', '*', '/', '+', '!', 'not', 'and', 'or', 'xor', 'sin'}

    ALL_OPERATIONS = SPACE_CONST | MATH_CONST.keys() | BRACKETS | DUALISTIC_OPERATIONS.keys() | STANDART_OPERATIONS

    # Operation: (op, unary/binary type, prefix/infix/postfix type, prior)    
    OPERATIONS = {
        '^':        (operator.pow, INFIX_OP, BIN_OP, 10),
        '*':        (operator.mul, INFIX_OP, BIN_OP, 20),
        '/':        (operator.truediv, INFIX_OP, BIN_OP, 20),
        '+':        (operator.add, INFIX_OP, BIN_OP, 30),
        '-':        (operator.sub, INFIX_OP, BIN_OP, 30),
        '-#':       (operator.neg, PREFIX_OP, UNARY_OP, 10),
        '!':        (math.factorial, POSTFIX_OP, UNARY_OP, 10),
        'not':      (operator.not_, PREFIX_OP, UNARY_OP, 10),
        'and':      (operator.and_, INFIX_OP, BIN_OP, 20),
        'or':       (operator.or_, INFIX_OP, BIN_OP, 30),
        'xor':      (operator.xor, INFIX_OP, BIN_OP, 30),
        'sin':      (math.sin, PREFIX_OP, UNARY_OP, 5),
    }

    def __init__(self, expr_str, isDAL = True) -> None:
        if isDAL:
            self.expr_dal_str = expr_str
            self.expr_rpn_str = None
        else:
            self.expr_dal_str = None
            self.expr_rpn_str = expr_str

        self.expr_dal = None
        self.expr_rpn = None

    # TO-DO: проверить корректность выражения: подряд идущие операции и т.п.
    def convertStrToListExpr(self):
        def splitOperatorsAndOperands(expr_str):
            if not expr_str: return []

            isOperator = False if expr_str[0].isdigit() else True

            result = []
            curr_index = 0
            while curr_index < len(expr_str):
                buffer = []

                isInt = True
                while isOperator and curr_index < len(expr_str) and not (expr_str[curr_index].isdigit() or expr_str[curr_index] == '.'):
                    if expr_str[curr_index] == '.': isInt = False
                    buffer.append(expr_str[curr_index])
                    curr_index += 1

                while not isOperator and curr_index < len(expr_str) and (expr_str[curr_index].isdigit() or expr_str[curr_index] == '.'):
                    buffer.append(expr_str[curr_index])
                    curr_index += 1
                
                if isOperator:
                    result.append(''.join(buffer))
                else:
                    if isInt:
                        result.append(int(''.join(buffer)))
                    else:
                        result.append(float(''.join(buffer)))

                isOperator = not isOperator
        
            return result
        
        def splitOperators(operators):
            if operators in Calculator.ALL_OPERATIONS: return [operators]

            stack = [([], '', 0)]
            while stack:
                curr_result, curr_buffer, curr_index = stack.pop()

                if curr_index < len(operators):
                    next_buffer = curr_buffer+operators[curr_index]

                    stack.append((curr_result, next_buffer, curr_index+1))
                    if next_buffer in Calculator.ALL_OPERATIONS:
                        stack.append((curr_result+[next_buffer], '', curr_index+1))
                else:
                    if curr_buffer == '': return curr_result

            raise OperatorError(f'expression contains an unsupported operation: {operators}')
        
        def splitOperatorsInList(expr):
            result = []

            for ch in expr:            
                if isinstance(ch, Number):
                    result.append(ch)
                else:
                    result.extend(splitOperators(ch))

            return result
               
        def skipSpaceAndGetConst(expr):
            result = [x for x in expr if x not in Calculator.SPACE_CONST]

            for i in range(len(result)):
                if result[i] in Calculator.MATH_CONST: result[i] = Calculator.MATH_CONST[result[i]]

            return result

        def realiseDualisticOperation(expr):
            result = []

            for i in range(len(expr)):
                ch = expr[i]

                if ch in Calculator.DUALISTIC_OPERATIONS:
                    if i == 0 or not (isinstance(expr[i-1], Number) or expr[i-1] in Calculator.CLOSING_BRACKETS or (expr[i-1] in Calculator.OPERATIONS and Calculator.OPERATIONS[expr[i-1]][1] == Calculator.POSTFIX_OP)):
                        result.append(Calculator.DUALISTIC_OPERATIONS[ch][0])
                    else:
                        result.append(Calculator.DUALISTIC_OPERATIONS[ch][1])
                else:
                    result.append(ch)

            return result
        
        def isValidBrackets(expr):
            stack = []

            for ch in expr:
                if ch in Calculator.OPENING_BRACKETS:
                    stack.append(ch)
                elif ch in Calculator.CLOSING_BRACKETS:                    
                    if stack and Calculator.BRACKETS_MAP[stack[-1]] == ch:                        
                        stack.pop()
                    else:
                        return False
                    
            if not stack:
                return True
            else:
                return False
                
        if self.expr_dal_str is not None:
            result = self.expr_dal_str
        else:
            result = self.expr_rpn_str

        result = splitOperatorsAndOperands(result)
        result = splitOperatorsInList(result)
        result = skipSpaceAndGetConst(result)
        result = realiseDualisticOperation(result)
        
        if isValidBrackets(result):
            self.expr_dal = result
        else:
            raise BracketsSeqError('expression contains an invalid parenthesis sequence')

    def convertDALtoRPN(self):
        expr = self.expr_dal
        
        result, stack = [], []        
        
        for ch in expr:
            if isinstance(ch, Number) or (ch in Calculator.OPERATIONS and Calculator.OPERATIONS[ch][1] == Calculator.POSTFIX_OP):
                result.append(ch)
            elif (ch in Calculator.OPERATIONS and Calculator.OPERATIONS[ch][1] == Calculator.PREFIX_OP) or (ch in Calculator.OPENING_BRACKETS):
                stack.append(ch)
            elif (ch in Calculator.CLOSING_BRACKETS):
                while stack[-1] not in Calculator.OPENING_BRACKETS:
                    result.append(stack.pop())
                stack.pop()
            elif (Calculator.OPERATIONS[ch][2] == Calculator.BIN_OP):
                while stack and stack[-1] not in Calculator.BRACKETS and \
                        ((Calculator.OPERATIONS[stack[-1]][1] == Calculator.PREFIX_OP or Calculator.OPERATIONS[stack[-1]][3] <= Calculator.OPERATIONS[ch][3])):                    
                    result.append(stack.pop())
                stack.append(ch)

        while stack:
            result.append(stack.pop())

        self.expr_rpn = result

    def calculateRPN(self):        
        self.convertStrToListExpr()       
        if self.expr_rpn is None: self.convertDALtoRPN()        
        expr = self.expr_rpn

        stack = []
        for ch in expr:
            if isinstance(ch, Number):
                stack.append(ch)
            else:
                if Calculator.OPERATIONS[ch][2] == Calculator.UNARY_OP:
                    stack.append(Calculator.OPERATIONS[ch][0](stack.pop()))                
                elif Calculator.OPERATIONS[ch][2] == Calculator.BIN_OP:
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(Calculator.OPERATIONS[ch][0](a, b))

        if len(stack) != 1: raise ExpressionError('expression has wrong operators or operand sequence')
        return stack.pop()
    

if __name__ == '__main__':
    test_exp = '-10 + 3!*2+2^3-sin(pi/2)'
    res = Calculator(test_exp).calculateRPN()
    print(f'{test_exp} = {res}')

    test_exp = '((2+2)^2)'
    res = Calculator(test_exp).calculateRPN()
    print(f'{test_exp} = {res}')