
################### Scope ####################

enemies = 1

def increase_enemies(): #function will take the variable inside
  global enemies #will take the global enemy and will modify it
  #you dont want to do this often/prone to generate bugs/ more easy to fail
  print(f"enemies inside function: {enemies}")
  return enemies +1

increase_enemies() #here we are going to print 2
print(f"enemies outside function: {enemies}")  #prints 1 because of the scope

#There is no block scope
#what is a block scope

enemmies = ["skeleton", "zombie", "Alien"]
game_level = 3
if game_level < 5:
  new_enemy = enemmies[0]
print(new_enemy)

#Global scope can be used for constant like the constant pi 

PI = 3.1416
URL = "google.com"
TWITTER_HANDLE = "@tony"







