
def answers(first_operand_list, operator_list, second_operand_list):
  answers_list = []
  answers_line = ''
  i = 0
  while i < len(first_operand_list):
    if operator_list[i] == '+':
      answers_list.append(str(int(first_operand_list[i]) + int(second_operand_list[i])))
    elif operator_list[i] == '-':
      answers_list.append(str(int(first_operand_list[i]) - int(second_operand_list[i])))
    i += 1
  # print(answers_list)
  i = 0
  while i < len(answers_list):
    answers_line += ((max(len(first_operand_list[i]), len(second_operand_list[i]))) + 2 - len(answers_list[i])) * ' '
    answers_line += answers_list[i]
    if i != len(answers_list) - 1:
      answers_line += 4 * ' '
    i += 1
  # print(answers_line)
  return answers_line

def put_dash(longest_operand):
  dash_line = ''
  i = 0
  while i < len(longest_operand):
    dash_line += (2 + longest_operand[i]) * '-'
    if i != len(longest_operand) - 1:
      dash_line += 4 * ' '
    i += 1
  return dash_line

def arithmetic_arranger(problems, boolean=None):
  arranged_problems = ''
  first_operand_list = []
  second_operand_list = []
  operator_list = []
  longest_operand = []
## Error Management
  if len(problems) > 5:
    return "Error: Too many problems."
#   print(problems)
  for problem in problems:
    operation = problem.split()
    # print(operation)
    if len(operation) > 3:
      return "Error."
    if operation[1] != '+' and operation[1] != '-':
      return "Error: Operator must be '+' or '-'."
    if operation[0].isdigit() == False or operation[2].isdigit() == False:
      return "Error: Numbers must only contain digits."
    if len(operation[0]) > 4 or len(operation[2]) > 4:
      return "Error: Numbers cannot be more than four digits."
## Parsing into 3 lists
    first_operand_list.append(operation[0])
    operator_list.append(operation[1])
    second_operand_list.append(operation[2])
#   print("FIRST",first_operand_list)
#   print("OPRTR",operator_list)
#   print("SECND",second_operand_list)
## First line
  i = 0
  while i < len(problems):
    longest_operand.append(max(len(first_operand_list[i]), len(second_operand_list[i])))
    arranged_problems += first_operand_list[i].rjust(longest_operand[i] + 2)
    arranged_problems += 4 * ' ' if i != len(first_operand_list) - 1 else '\n'
    i += 1
## Second line
  i = 0
  while i < len(problems):
    arranged_problems += operator_list[i]
    arranged_problems += second_operand_list[i].rjust(longest_operand[i] + 1)
    arranged_problems += 4 * ' ' if i != len(first_operand_list) - 1 else '\n'
    i += 1
## Third line: Dash line
  arranged_problems += put_dash(longest_operand)
## Fourth line: Answer line
  if boolean is True:
    arranged_problems += '\n'+ answers(first_operand_list, operator_list, second_operand_list)
  return arranged_problems

def main():
  print(arithmetic_arranger(['3801 - 2', '123 + 49', '1 - 9380']))
  print(arithmetic_arranger(['1 + 2', '1 - 9380']))
  print(arithmetic_arranger(['3 + 855', '3801 - 2', '45 + 43', '123 + 49']))
  print(arithmetic_arranger(['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380']))
  print(arithmetic_arranger(['3 + 855', '988 + 40'], True))
  print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))

main()
