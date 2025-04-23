#welcome and ask user for name
user_name = input("Hi, welcome to a trivia game of SDG14. What's your name :"). capitalize()

#ask user if they want to play
user_response = input("Wanna play(yes or no): "). lower()
positive_response = "yes"
if user_response == positive_response:
    print(f"Cool, lets start {user_name}!")
else:
    print("Oh well, see you next time.")