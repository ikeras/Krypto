from enum import Enum, auto

class TokenKind(Enum):
    NUMBER = auto()
    OPEN_PAREN = auto()
    CLOSE_PAREN = auto()
    PLUS = auto()
    MINUS = auto()
    MOD = auto()
    SQUARE_ROOT = auto()
    MULTIPLY = auto()
    DIVIDE = auto()
    EXPONENTIATION = auto()