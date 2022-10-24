# normal way

from audioop import add
from email.charset import add_alias


numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
new_list.append(add_1)

# list comprenhension
# Syntax
'''
new_list = [new_item for item in list    ]
'''
name = "Tony"
new_list = [n for n in name]

new_list = [n*n for n in range(1, 5) if n % 2 == 0]

# names = ["Alex", "Beth", "Caronline", "Dave", "Eleanor", "Freddie"]
# new_list = [name.upper() for name in names if len(name) > 5]
print(new_list)
