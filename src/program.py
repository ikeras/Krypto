from collections import Counter
from math_expression import MathExpression
from problem import Problem

print('This a math game where the goal is to create an expression using 5 provided numbers')
print('that evaluates to the goal number. For example, if the goal number is 13 and the')
print('provided numbers are 2, 6, 4, 5, and 6 then a correct answer would be: 2 + 6 - 5 + 4 + 6.')
print('The only operators that may be used are +, -, *, /. Order of operations apply but can be')
print('overridden using parantheses. Good luck and have fun!')
print()

user_input = ''
count = 0
solved = 0
while True:
    count += 1
    problem = Problem(5)
    print(f'Problem #{count}')
    print(f'Goal: {problem.result}')
    print('Operands:', end=' ')
    print(*problem.operands)
    print()
    user_input = input('Your expression guess: ')
    
    if user_input == 'exit':
        break
    
    try:
        expression = MathExpression(user_input)
        
        if Counter(expression.operands) == Counter(problem.operands):
            if expression.result == problem.result:
                solved += 1
                print('Excellent job! You have solved this correctly!')
            else:
                print(f'Unfortunately, the expected result was {problem.result} and your result was {expression.result}')
                print(f'A possible solution would have been {problem.calculated_expression}')
        else:
            print('Unfortunately, you did not use the correct operands.')
            print('Expected:', end=' ')
            print(*problem.operands)
            print('Used', end=' ')
            print(*expression.operands)
    except ValueError as err:
        print(f'Unfortunately your expression guess resulted in an error: {err}.')

    print()
    
print(f'You solved {solved} out of {count} problems!')