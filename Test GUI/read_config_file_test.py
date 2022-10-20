given_file = open('Configuration Files/Calcium.txt', 'r')

lines = given_file.readlines()

config = []

for line in lines:
    empty_str = ""
    for c in line:
        if c.isdigit() == True:
            empty_str += c
    if empty_str.isdigit():
        config.append(int(empty_str))

print(config)
