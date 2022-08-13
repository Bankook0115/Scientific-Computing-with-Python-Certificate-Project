import re

def arithmetic_arranger(problems, solve = False): #ini value solve = false
  #this
  #"32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

  #into this
  #"   32   3801   45   123\n+ 698    -2     +43  +49\n -----  ------  ---- -----"
  if len(problems) > 5:
    return "Error: Too many problems."
  
  first = ""
  second = ""
  lines = ""
  sumx = ""
  arranged_problems = ""
  for problem in problems:
    #check error
    if(re.search("[^\s0-9,+-]",problem)):
      if(re.search("[/]",problem) or re.search("[*]",problem)):
        return "Error: Operator must be '+' or '-'."
      return "Error: Numbers must only contain digits."

    #start separate the data
    firstNumber = problem.split(" ")[0]
    operator = problem.split(" ")[1]
    secondNumber = problem.split(" ")[2]

    if (len(firstNumber) > 4 or len(secondNumber) > 4):
      return "Error: Numbers cannot be more than four digits."

    result = "" # string
    if (operator == "+"):
      result = str(int(firstNumber) + int(secondNumber))
    elif (operator == "-"):
      result = str(int(firstNumber) - int(secondNumber)) #operator !!!

    length = max(len(firstNumber),len(secondNumber)) + 2
    top = str(firstNumber).rjust(length)
    bottom = str(operator) + str(secondNumber).rjust(length - 1)
    line = ""
    res = str(result).rjust(length)
    for i in range(length):
      line += "-"

    if problem != problems[-1]: #check it's not last item on problems list
      first += top + '    '
      second += bottom + '    '
      lines += line + '    '
      sumx += res + '    '
    else:
      first += top
      second += bottom
      lines += line
      sumx += res

  if solve:
    arranged_problems = first + "\n" + second + "\n" + lines + "\n" + sumx
  else:
    arranged_problems = first + "\n" + second + "\n" + lines
    
  return arranged_problems