def Decode(input):
  new_pass = ''
  for i in range(len(input)):
    if input[i] <= 2:
      new_pass += input[i] + 7
    else:
      new_pass += input[i] - 3
  return [new_pass, input]

def encoder(password):
  new_pass = ''
  for number in password:
    if int(number)+3 >= 7:
      new_pass += (int(number) - 7)
    else:
      new_pass += (int(number) + 3)
  return new_pass

def menu():
  print("Menu")
  print("-------------")
  print("1. Encode")
  print("2. Decode")
  print("3. Quit")

def main():
  while True:
    menu()
    option = int(input("Please enter an option: "))
    if option == 1:
      input = input("Please enter your password to encode: ")
      encoder(input)
      print("Your password has been encoded and stored!")
    elif option == 2:
      value = Decode(option)
      print(f"The encoded password is {value[1]}, and the original password is {value[0]}")
    elif option == 3:
      break
  
