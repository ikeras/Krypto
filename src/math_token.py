from tokenkind import TokenKind
from associativity import Associativity

class MathToken:
    def __init__(self, kind, value=-1, precedence=-1, associativity=Associativity.NONE):
        self.kind = kind
        self.value = value
        self.precedence = precedence
        self.associativity = associativity
        
    def is_operator(self):
        return ((self.kind == TokenKind.DIVIDE) or
                (self.kind == TokenKind.MINUS) or
                (self.kind == TokenKind.MOD) or
                (self.kind == TokenKind.EXPONENTIATION) or
                (self.kind == TokenKind.MULTIPLY) or
                (self.kind == TokenKind.PLUS) or
                (self.kind == TokenKind.SQUARE_ROOT))

    def __str__(self):
        result = f'Token {self.kind} '
        
        if self.kind == TokenKind.NUMBER:
            result += f'Value: {self.value}'
        elif self.is_operator():
            result += f'Associativity: {self.associativity} Precedence: {self.precedence}'
        
        return result
