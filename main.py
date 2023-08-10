# Odd or Even Exercise: Write an app that will let you know if user input is an even or odd number
#number = int(input("Which number do you want to check? "))


# if number % 2 > 0:
#  print ("Odd")
# else:
#  print ("Even")

print("Welcome to the rollercoaster! ")
height = int(input("What is your height in cm? "))

bill = 0

if height >= 120: 
  print("You are tall enough to ride! ")
  age = int(input("What is your age? "))
  
  if age >= 19: 
      bill = 12
      print ("Adult price is $12 ")
  elif age <=11:
    bill = 5
    print("Child price is $5 ")
  else:
    bill = 7
    print("Youth price is $7 ")

  wants_photo = input("Do you want to add a photo for $3 Y/N? ")
  if wants_photo == "Y":
  #Add $3 to bill, we'll need a var 
    bill += 3
  
  print(f"Your total is {bill}.")

else: 
  print("Sorry, you're not quite tall enough to ride. ")





