# Dict comprehension
# syntax
'''
new_dict = {new_key:new value for (key:value) in dict.items() if test}
'''
from random import randint
import pandas

# student_scores = {
#     "Alex": 89,
#     "Beth": 90
# }

# names = ["Alex", "Beth", "Caronline", "Dave", "Eleanor", "Freddie"]

# new_scores = {student: randint(1, 100) for student in names}
# print(new_scores)

# new_new_scores = {student: score for (
#     student, score) in new_scores.items() if score > 60}
# print(new_new_scores)

# sentence = "what is the airspeed of a bird in the air?"

# new_dict = {word: len(word) for word in sentence.split(' ')}
# print(new_dict)

student_scores = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

students_data = pandas.DataFrame(student_scores)

for (index, row) in students_data.iterrows():
    print(row.score)
