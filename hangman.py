from random_word import RandomWords

name = input("Enter your name: ")

print(f"Welcome, {name}.")

print("Start guessing...")

r = RandomWords()

answer = r.get_random_word()

print(answer)
guesses = ''

turns = 10

while turns > 0:

    failed = 0

    for char in answer:

        if char in guesses:
            if answer.index(char) != len(answer) - 1:
                print(char, end="")
            else:
                print(char)

        else:
            if answer.index(char) != len(answer) - 1:
                print("_", end="")
            else:
                print("_")

            failed += 1

    if failed == 0:
        print("You won")
        break
    guess = input("Guess a character: ")

    guesses += guess

    if guess not in answer:

        turns -= 1

        print("Wrong")

        print("You have", + turns, 'more guesses')

        if turns == 0:
            print("You Lose")