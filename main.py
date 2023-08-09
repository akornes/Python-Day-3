# Odd or Even Exercise: Write an app that will let you know if user input is an even or odd number
#number = int(input("Which number do you want to check? "))


# if number % 2 > 0:
#  print ("Odd")
# else:
#  print ("Even")

print("Welcome to the rollercoaster! ")
height = int(input("What is your height in cm? "))

if height >= 120: 
  print("You are tall enough to ride! ")
  age = int(input("What is your age? "))
  
  if age >= 19: 
      print ("Please pay $12 ")
  elif age <=11:
    print("Please pay $5 ")
  else:
    print("Please pay $7 ")

else: 
  print("Sorry, you're not quite tall enough to ride. ")





