#one relationship in our code
#what is OOP? Split in multiple pieces
#pieces are reusable
#imagine resto, multiple positions, hard to manage if one man army
#Manager -> Chef, Waiter, Cleaner

#model waiter, what it has and what it does

#integrate packages -> PyPi open source

import turtle
from prettytable import PrettyTable

timmy = turtle.Turtle()

# screen = turtle.Screen()
# print(screen.canvheight) #printing attribute
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)