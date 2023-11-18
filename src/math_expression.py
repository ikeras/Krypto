from associativity import Associativity
from collections import deque
from math import sqrt
from math_token import MathToken
from scanner import Scanner
from tokenkind import TokenKind

class MathExpression:
    def __init__(self, input):
        self._input = input
        self.operands = []
        self._scanner = Scanner(self._input)
        self._postfix_expression = self.convert_to_postfix()
        self.result = (int)(self.evaluate())

    # Convert to postfix (reverse polish notation) using the shunting yard algorithm
    # http://en.wikipedia.org/wiki/Shunting-yard_algorithm        
    def convert_to_postfix(self):
        output = deque()
        operators = deque()
        
        for token in self._scanner.iter_tokens():
            if token.kind == TokenKind.NUMBER:
                output.append(token)
                self.operands.append(token.value)
            elif token.is_operator():
                while len(operators) > 0:
                    o2 = MathExpression.peek_stack(operators)
                    
                    if ((token.associativity == Associativity.LEFT and token.precedence <= o2.precedence) or
                        (token.associativity == Associativity.RIGHT and token.precedence < o2.precdence)):
                        o2 = operators.pop()
                        output.append(o2)
                    else:
                        break
                
                operators.append(token)
            elif token.kind == TokenKind.OPEN_PAREN:
                operators.append(token)
            elif token.kind == TokenKind.CLOSE_PAREN:
                open_paren_found = False
                
                while not open_paren_found and len(operators) > 0:
                    o2 = operators.pop()
                    
                    if o2.kind == TokenKind.OPEN_PAREN:
                        open_paren_found = True
                    else:
                        output.append(o2)
                    
                if not open_paren_found:
                    raise ValueError('Found extra closing paranthesis')
        
        while len(operators) > 0:
            o2 = operators.pop()
            
            if o2.kind == TokenKind.OPEN_PAREN or o2.kind == TokenKind.CLOSE_PAREN:
                raise ValueError('Found extra parantheses')
            
            output.append(o2)
        
        return output    
    
    @staticmethod
    def peek_stack(stack):
        if stack:
            return stack[-1]
        else:
            return None
        
    @staticmethod
    def perform_binary_operation(operands, eval):
        if len(operands) < 2:
            raise ValueError('The operand stack contains too few operands for the binary operation')
        
        operand2 = operands.pop()
        operand1 = operands.pop()
        
        if operand1.kind != TokenKind.NUMBER or operand2.kind != TokenKind.NUMBER:
            raise ValueError(f'Expected two numbers for the binary expression, but found: {operand1} {operand2} instead')
        
        return MathToken(TokenKind.NUMBER, value=eval(operand1.value, operand2.value))
    
    @staticmethod
    def perform_unary_operation(operands, eval):
        if len(operands) < 1:
            raise ValueError('The operand stack contains too few operands for the unary operation')
        
        operand = operands.pop()
        
        if operand.kind != TokenKind.NUMBER:
            raise ValueError(f'Expected a number as the operand for the unary expression, but found: {operand}')
        
        return MathToken(TokenKind.NUMBER, eval(operand.value))
    
    def evaluate(self):
        operands = deque()
        
        while len(self._postfix_expression) > 0:
            token = self._postfix_expression.popleft()
            
            if token.is_operator():
                if token.kind == TokenKind.PLUS:
                    operands.append(MathExpression.perform_binary_operation(operands, lambda a, b: a + b))
                elif token.kind == TokenKind.MINUS:
                    operands.append(MathExpression.perform_binary_operation(operands, lambda a, b: a - b))
                elif token.kind == TokenKind.MOD:
                    operands.append(MathExpression.perform_binary_operation(operands, lambda a, b: a % b))
                elif token.kind == TokenKind.MULTIPLY:
                    operands.append(MathExpression.perform_binary_operation(operands, lambda a, b: a * b))
                elif token.kind == TokenKind.DIVIDE:
                    operands.append(MathExpression.perform_binary_operation(operands, lambda a, b: a // b))
                elif token.kind == TokenKind.SQUARE_ROOT:
                    operands.append(MathExpression.perform_unary_operation(operands, lambda a: sqrt(a)))
                elif token.kind == TokenKind.EXPONENTIATION:
                    operands.append(MathExpression.perform_binary_operation(operands, lambda a,b: a ** b))
                else:
                    raise ValueError(f'Expected operator, but got: {token}')
            else:
                if token.kind != TokenKind.NUMBER:
                    raise ValueError(f'Expected number token, but got: {token}')
                
                operands.append(token)
        
        if len(operands) != 1:
            raise ValueError('There were too many operators in the expression for the number of operands')
        
        result = operands.pop()
        
        if result.kind != TokenKind.NUMBER:
            raise ValueError('The expression resulted in an illegal output (not a number)')
        
        return result.value
    