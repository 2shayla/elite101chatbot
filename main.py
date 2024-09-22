print("Welcome to the Elite101 Chatbot!")
name = input("Please enter your name.")
print(f'Nice to meet you,{name}!')
age = input(f"How old are you {name}?")
print(f"Wow,you're {age} years young.")

def display_menu():
  print("\n **Options**")  
  print("1. View Store Hours ") 
  print("2. Store Location Details")
  print("3. Store Contact Information")
  print("4. Exit\n")

def user_selection():
  in_use = True 
  user_input = int(input("Enter a number between 1-4: "))
  if user_input == 1:
      print("The store hour is from 8am to 8pm")
  elif user_input == 2:
      print("The store is located in the heart of New York")
  elif user_input == 3:
      print("The store contact information can be found at the bottom of the web page")
  elif user_input == 4:
      print(f'It was nice speaking to you {name}!')
      in_use = False
  else: 
      print("Please provided a valid number")
  return in_use

program_run = True

while program_run:
    display_menu()
    program_run = user_selection()
