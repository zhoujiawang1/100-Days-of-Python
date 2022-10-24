# FileNotFound
'''
with open("file.txt") as file:
    file.read()

'''

# KeyError
'''
a_dict = {key:value}
value = a_dict['nothing']
'''

# IndexError
#fruits = [1,2,3]
#fruit = fruits[3]

# TypeError
#text = abc
# print(text+5)

# Error handling
'''
try: #might cause an error

except: do this if there was an exception

else: do this if no exception

finally: do this no matter what happens

'''
# try:
#     file = open("file.txt")

# # careful for all errors that might be in the try block
# except FileNotFoundError:  # want to catch a specific error
#     file = open("file.txt", "w")
# except KeyError as error_message:
#     print(error_message)
# else:
#     print("File was opened")
# finally:
#     file.close()
#     print("File closed")

# #How to raise own exceptions
#     # raise TypeError("Made up error")

# height = float(input("height"))
# weight = int(input("weight"))

# if height > 3:
#     raise ValueError("Height shouldnt be over 3")

fruits = ["Apple", "Banana", "Orange"]


def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("fruit pie")
    else:
        print(fruit + " pie")


make_pie(4)
