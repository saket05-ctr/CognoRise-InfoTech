def add():
  n1=int(input("Enter first number:"))
  n2=int(input("Enter second number:"))
  return n1+n2

def subtract():
  n1=int(input("Enter first number:"))
  n2=int(input("Enter second number:"))
  return n1-n2

def multiply():
  n1=int(input("Enter first number:"))
  n2=int(input("Enter second number:"))
  return n1*n2

def divide():
  n1=int(input("Enter divident number:"))
  n2=int(input("Enter divisor number:"))
  return n1/n2

print('welcome to the calculator')
print(f"1.addition(+)\n2.subtraction(-)\n3.multiplicattion(*)\n4.division(/)")
operation =input("what operation you want to perform: ")

if operation== '1' or operation=='+':
  result=add()
  print(f"result of addtion is {result}")

elif operation== '2' or operation =='-':
  result=subtract()
  print(f"result of subtraction is {result}")

elif operation== '3' or operation =='*':
  result=multiply()
  print(f"result of multiplication is {result}")

elif operation== '4' or operation =='/':
  result=divide()
  print(f"result of division is {result}")

else:
  print("choose correct operation again!!")
print("Thank you for using the calculator..")