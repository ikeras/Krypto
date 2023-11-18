from math_expression import MathExpression
from random import Random

class Problem:
    def __init__(self, num_operands):
        self.operands = []
        
        random = Random()
        current_value = random.randint(1, 9)
        
        calculated_expression = '((((' + str(current_value)
        
        self.operands.append(current_value)
        
        for i in range(0, num_operands - 1):
            operand = random.randint(1, 9)
            
            self.operands.append(operand)
            
            symbol = ''
            
            op = random.randint(0, 3)
            
            # case +
            if op == 0:
                if current_value > 30 and current_value - operand > 0:
                    symbol = '-'
                    current_value -= operand
                else:
                    symbol = '+'
                    current_value += operand
            # case -
            elif op == 1:
                if current_value - operand > 0:
                    symbol = '-'
                    current_value -= operand
                else:
                    symbol = '+'
                    current_value += operand
            # case *
            elif op == 2:
                if current_value > 30 and current_value % operand == 0 and current_value > operand:
                    symbol = '/'
                    current_value /= operand
                elif current_value > 30 and current_value - operand > 0:
                    symbol = '-'
                    current_value -= operand
                else:
                    symbol = '*'
                    current_value *= operand
            # case /
            else:
                if current_value % operand == 0 and current_value > operand:
                    symbol = '/'
                    current_value /= operand
                elif current_value - operand > 0:
                    symbol = '-'
                    current_value -= operand
                else:
                    symbol = '+'
                    current_value += operand
            
            calculated_expression += f' {symbol} {operand})'
        
        random.shuffle(self.operands)
        
        math_expression = MathExpression(calculated_expression)
        
        self.result = math_expression.result
        self.calculated_expression = calculated_expression