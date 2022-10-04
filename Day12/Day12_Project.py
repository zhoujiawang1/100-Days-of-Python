import random
print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100")
mode = (input("Choose a difficulty. Type 'easy' and 'hard': "))
number = random.randrange(1,100)

def indicate_direction(guess, number, chances):
    if guess > number:
        print("Too high")
        print("Guess again")
        chances -= 1
    elif guess < number:
        print("Too low")
        print("Guess again")
        chances -= 1
    return chances

def check_game(guess, number, game):
    if guess == number:
        game = False
        print("You win!")
    elif chances <= 0:
        game = False
        print("You lose")
    return game


while mode != "easy" and mode != "hard":
    mode = input("Choose a difficulty. Type 'easy' and 'hard': ")

if mode == "easy":
    chances = 10
elif mode == "hard":
    chances = 5

print(number)
game = True
print(f"You have {chances} attempts remaining to guess the number")
guess = int(input("Make a guess: "))
while game:
    print(f"You have {chances} attempts remaining to guess the number")
    chances = indicate_direction(guess, number, chances)
    guess = int(input("Make a guess: "))
    game = check_game(guess, number, game)
    
