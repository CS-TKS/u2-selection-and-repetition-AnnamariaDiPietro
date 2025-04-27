#welcome and ask user for name
user_name = input("Hi, welcome to a trivia game about overfishing. What's your name? :"). capitalize()

#ask user if they want to play
user_response = input("Wanna play(yes or no)?: "). lower()
positive_response = "yes"
if user_response == positive_response:
    print(f"Cool, lets start {user_name}!")
else:
    print("Oh well, see you next time.")
    quit()

#first question with while loop
correct_answer = "14"
tries = 0
max_tries = 3

while tries<max_tries:
    answer = input("What SDG do you think overfishing belongs to(numbers only)? :")
    if answer == correct_answer:
        print("Correct, good job!")
        tries = 3
    else:
        tries += 1
        if tries<max_tries:
            print(f"Nope, you have {max_tries - tries} left.")
        else:
            print(f"Sorry {user_name} all you tries have been used up.")
            print("The correct answer was SDG 14, life below water.")


