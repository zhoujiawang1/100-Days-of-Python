from art import *
from game_data import data
import random
import os

def check_follow(A, B):
    if A['follower_count'] > B['follower_count']:
        return True
    else:
        return False
    

def disp_choices(PersonA, PersonB):
    print(f"Comapre A: {PersonA['name']}, a {PersonA['description']}, from {PersonA['country']}")
    print(vs)
    print(f"Comapre B: {PersonB['name']}, a {PersonB['description']}, from {PersonB['country']}")

def add_score(game_status, score):
    if game_status:
        return score + 1
    else:
        return score

original_data = data
PersonA = random.choice(data)
new_data = data.pop(data.index(PersonA))
PersonB = random.choice(data)
print(logo)
disp_choices(PersonA, PersonB)

choice = ''

while choice != 'A' and choice !='B':
    choice = input("Who has more follofwers? Type 'A' or 'B': ")

game = True
score = 0 

if choice == 'A':
    game = check_follow(PersonA, PersonB)
else:
    game = check_follow(PersonB, PersonA)
score = add_score(game, score)


while game:
    os.system('cls')
    print(logo)
    print(f"You're right! Current score: {score}")

    data = original_data
    original_data = data
    PersonA = random.choice(data)
    new_data = data.pop(data.index(PersonA))
    PersonB = random.choice(data)

    disp_choices(PersonA, PersonB)
    choice = input("Who has more follofwers? Type 'A' or 'B': ")

    if choice == 'A':
        game = check_follow(PersonA, PersonB)
    else:
        game = check_follow(PersonB, PersonA)

    score = add_score(game, score)

os.system('cls')
print(logo)
print(f"You lost, Final score {score}")

