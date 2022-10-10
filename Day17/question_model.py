class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def check_answer(self, ans):
        if self.answer == ans:
            return True
        else:
            return False

    