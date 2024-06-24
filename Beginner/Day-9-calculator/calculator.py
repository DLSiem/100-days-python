from art import logo
from replit import clear

print(logo)

end = False

def add(n1, n2):
  return n1 + n2
def sub(n1, n2):
  return n1 - n2
def mul(n1, n2):
  return n1 * n2
def div(n1, n2):
  return n1 / n2

while not end:
  n1 = float(input("What's the first number?: "))
  print("+\n-\n*\n/")
  operation = input("Pick an operation: ")
  n2 = float(input("What's the next number?: "))
  result = None
  if operation == "+":
    result = add(n1, n2)
  elif operation == "-":
    result = sub(n1, n2)
  elif operation == "*":
    result = mul(n1, n2)
  elif operation == "/":
    result = div(n1, n2)
  else:
    print("Invalid operation")
    continue

  print(f"{n1} {operation} {n2} = {result}")
  cont = input(f"Type 'y' to continue calculating with {result}, or type 'n' to quit.")
  if cont == 'n':
    end = True
  else:
    clear()

