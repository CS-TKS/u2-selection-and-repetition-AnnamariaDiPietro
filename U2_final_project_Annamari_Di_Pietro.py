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

#a space so that it looks neater when the user plays
print(" ")

#list of answers for questions
#not all the questions
correct_answers = [
    "14",      # Q1: SDG number
    "true",    # Q3: 90% predatory fish
]

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

#a space so that it looks neater when the user plays
print(" ")

#second question with boolean statement
#when too many fish in a particular stock are caught and there are not enough adults to breed and sustain a healthy population
answer_for_Q2 = input("Is overfishing when too many fish are caught and the population cannot recover?(True/False) :")
print(answer_for_Q2.capitalize() == "True")

#a space so that it looks neater when the user plays
print(" ")

#third question about % of fish stock thats already gone
#currently, wordldwide, 90% of of the stocks of large predatory fish, such as sharks, tuna, marlin, and swordfish, are already gone!
answer_for_Q3 = input("Are more than 90% of the worlds predatory fish gone already?(True/False) :")
print(answer_for_Q3.capitalize() == "True")

#a space so that it looks neater when the user plays
print(" ")

#fourth question
#tell user what governments can do about overfishinga and how they can make it sustainable
irr = "no"
print("A way that fishing can be more sustainble is if governments and big cooperations make laws. Such as increasing marine biodiversity protection.")
answer_for_Q4 = input("Do you want to know more about that(yes/no)?:")
if answer_for_Q4 == irr:
    print("Alright then.")
else:
    print("With protection, the biodiversity of the ecosystem will not crumble. There will be fish remaining that can reproduce and make new fish, keeping the life cycle going. Increase in protection does not mean that the fishing has to/will stop, it just means that it will be more sustainable. Sustainable fishing is when the rate, where the fish population lives does not decline, does not decline at an unnatural rate, over time because of fishing practices.")

#offer user sustainable solutions
print("A way that you can help out is by doing the following:")
print("Buy fish that has been approved by the certifications like the Marine Stewardship Council (MSC) or any other sustainable fishing certifications.")
print("Support local communities.")
print("Minimize fish intake.")

#a space so that it looks neater when the user plays
print(" ")

#ask if user is doing any of these at the moment
dont_mind_this = "yes"
response = input("Are you doing any of those at the moment?(yes/no) :")
if response == dont_mind_this:
    print("Great, just keep going!")
else:
    print("That's ok, you got this though!")

#a space so that it looks neater when the user plays
print(" ")

#ending
#saying why it matters
ran = "yes"
final = input("Are you aware that by 2048, will will run out of fish to eat.(yes/no)")
if final == ran:
    print("Good, because we potentially are the last generation to eat fish. Spread awareness, this is important")
else:
    print("By 2048 we will run out of seafood consumption, and that would lead to a massive ecological imbalance, and will possibly crumble the marine ecosystem, which will lead to even bigger problems.")

#a space so that it looks neater when the user plays
print(" ")

#call to action
print("Action is required.")

#a space so that it looks neater when the user plays
print(" ")

#thank user
print("Thank you for playing.")