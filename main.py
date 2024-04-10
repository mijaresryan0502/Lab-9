def Decode(input):
  new_pass = ''
  for i in range(len(input)):
    if input[i] <= 2:
      new_pass += input[i] + 7
    else:
      new_pass += input[i] - 3
  return [new_pass, input]
