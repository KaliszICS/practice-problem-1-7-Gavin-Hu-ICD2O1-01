

def q1():
  #Write code here
 print(True)
  


def q2():
  #Write code here
  user_input = input("Input an integer: ")
  number = int(user_input)
  result = number > 5
  print(result)
  print("false")

def q3():
  #Write code here
  user_input = input("Input the letter a: ")
  result = user_input == 'a'
  print(result)

def q4():
  #Write code here
  user_input = input("Input a word earlier in the dictionary than google: ")
  result = user_input < 'google'
  print(result)

def q5():
  #Write code here
  first_input = input("Input an integer: ")
  second_input = input("Input another integer: ")
  num1 = int(first_input)
  num2 = int(second_input)
  product = num1 * num2
  result = product > 40
  print("Your numbers multiplied together are greater than 40:", result)
  print("false")

#Do edit the code below
#Comment the lines below when running your tests

q1()
q2()
q3()
q4()
q5()
