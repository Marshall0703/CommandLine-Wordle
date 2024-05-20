import random
game_title = "Words Test"
word_bank = []
misplaced_guesses = []
incorrect_guesses = []
max_turns = 5 
turns_taken = 0


with open ("words.txt") as word_file:
    for line in word_file:
        word_bank.append(line.rstrip().lower())
       
word_to_guess = random.choice(word_bank)
print("Welcome to my", game_title)
print ("The word has", len(word_to_guess), "letters.")
print("You have", max_turns - turns_taken, "turns lefts")

while turns_taken < max_turns:
    guess = input("Guess The Word: ").lower()
    if len(guess) != len(word_to_guess) or not guess.isalpha():
        print("Please Enter the right length")
        continue
    index = 0
    for c in guess:
        if c == word_to_guess[index]:
            print(c, end=" ")
            if c in misplaced_guesses:
                misplaced_guesses.remove(c)
        elif c in word_to_guess:
            if c not in misplaced_guesses:
                misplaced_guesses.append(c)
            print("_", end=" ")
        else:
            if c not in incorrect_guesses:
                incorrect_guesses.append(c)
            print("_", end=" ")
        index += 1                           
    print("\n")
    print("Misplaced letters: ", misplaced_guesses)
    print("Incorrect letters: ", incorrect_guesses)
    turns_taken += 1

    if guess == word_to_guess:
        print("Congrats")
        break

    if turns_taken == max_turns:
        print("No good")
        break
    
print("YOu have", max_turns - turns_taken, "turns left")

