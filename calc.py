import re
def simple_calculator(expression):
    numbers = re.split(r'[+-]', expression)
    operands = re.findall(r'[+-]', expression)
    total = int(numbers[0])
    for i in range(len(numbers)-1):
        current_num = int(numbers[i+1])
        current_op = operands[i]
        if current_op == '+':
            total += current_num
        if current_op == '-':
            total -= current_num
    return total



my_expression = "1+2-4"
print(simple_calculator(my_expression))
