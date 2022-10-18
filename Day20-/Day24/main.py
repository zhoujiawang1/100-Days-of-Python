# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

file_name = open("Day20-24/Input/Names/invited_names.txt", "r")

names = file_name.readlines()

file = open("Day20-24/Input/Letters/starting_letter.txt")
content = file.read()
for name in names:
    new_name = name.replace("\n", "")
    letterfile = content.replace(" [name],", f" {new_name}")
    letter_name = name.replace("\n", "")
    letter = open(
        f"Day20-/Output/ReadyToSend/Letter_for_{letter_name}.txt", 'w')
    letter.write(letterfile)
    letter.close()

file.close()
file_name.close()
