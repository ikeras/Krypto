from math_token import MathToken
from associativity import Associativity
from tokenkind import TokenKind

class Scanner:    
    def __init__(self, input):
        self._input = input
    
    def iter_tokens(self):
        offset = 0
        input_length = len(self._input)
        
        while offset < input_length:
        
            # Skip whitespace
            while offset < input_length and self._input[offset].isspace():
                    offset += 1
        
            if offset < input_length:
                input_char = self._input[offset]
                
                if input_char == '√':
                    yield MathToken(TokenKind.SQUARE_ROOT, precedence=3, associativity=Associativity.RIGHT)
                    offset += 1
                elif input_char == '^':
                    yield MathToken(TokenKind.EXPONENTIATION, precedence=3, associativity=Associativity.RIGHT)
                    offset += 1
                elif input_char == '%':
                    yield MathToken(TokenKind.MOD, precedence=2, associativity=Associativity.LEFT)
                    offset += 1
                elif input_char == '*':
                    yield MathToken(TokenKind.MULTIPLY, precedence=2, associativity=Associativity.LEFT)
                    offset += 1
                elif input_char == '/':
                    yield MathToken(TokenKind.DIVIDE, precedence=2, associativity=Associativity.LEFT)
                    offset += 1
                elif input_char == '+':
                    yield MathToken(TokenKind.PLUS, precedence=1, associativity=Associativity.LEFT)
                    offset += 1
                elif input_char == '-':
                    yield MathToken(TokenKind.MINUS, precedence=1, associativity=Associativity.LEFT)
                    offset += 1
                elif input_char == '(':
                    yield MathToken(TokenKind.OPEN_PAREN)
                    offset += 1
                elif input_char == ')':
                    yield MathToken(TokenKind.CLOSE_PAREN)
                    offset += 1
                elif input_char.isdigit():
                    value = 0
                    
                    while offset < len(self._input) and self._input[offset].isdigit():
                        value = value * 10 + int(self._input[offset])
                        offset += 1
                    
                    yield MathToken(TokenKind.NUMBER, value=value)
                else:
                    raise ValueError(f'Unexpected input: {input_char}')
                            