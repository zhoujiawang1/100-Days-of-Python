from QuizBrain import QuizBrain
from data import question_data
from question_model import Question

question_bank = []
quiz = QuizBrain(question_bank)

for question in question_data:
    question_bank.append(Question(question['text'], question['answer']))

game = True

while quiz.still_has_questions():
    quiz.next_question()
quiz.end_game_msg()
