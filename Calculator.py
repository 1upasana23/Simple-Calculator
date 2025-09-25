# Simple Calculator

print("Welcome To The Simple Calculator...")

# Loop starts here":
while True:
  #Display the operations
  print("Select the operation to be performed:")
  print(1 , ". Addition (+)")
  print(2 , ". Subtraction (-)")
  print(3 , ". Multiplication (*)")
  print(4 , ". Division (/)")
  print(5 , ". Exit")

  # Take input from the user
  choice = input("Enter your choice:").strip()

  #Ends the loop
  if choice == "5":
    print("Thank you for using the calculator. GoodBye!!")
    break

  #Provide the inputs
  num1 = float(input("Enter your first number:"))
  num2 = float(input("Enter your second number:"))

  #Calculation
  if choice == "1":
    print("Addition Result:", num1 + num2)

  elif choice == "2":
    print("Subtraction Result:", num1 - num2)

  elif choice == "3":
    print("Multiplication Result:", num1 * num2)

  elif choice == "4":
    if num2 != 0:
      print("Division Result:", num1 / num2)
    else:
      print("Error! Division cannot be done by zero.")

  else:
    print("Invalid! Please select the valid option.")