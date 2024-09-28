from art import logo

#Calculator functions
def add(n1, n2):
  return n1 + n2


def subtract(n1, n2):
  return n1 - n2


def multiply(n1, n2):
  return n1 * n2


def divide(n1, n2):
  return n1 / n2


#need a dictionary to store the functions
operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
  print(logo)
  #Need n1, n2, and operator from the user
  n1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  #Ask the user if they want to continue with the answer
  should_continue = True

  while should_continue:
    operator = input("Pick an operation from the line above: ")
    n2 = float(input("What's the next number?: "))
    calculation_function = operations[operator]
    answer = calculation_function(n1, n2)
    print(f"{n1} {operator} {n2} = {answer}")

    if input(
        f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: "
    ) == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()


calculator()
