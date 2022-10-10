class QuizBrain:

    def __init__(self, q_list):
        self.q_number = 0
        self.q_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.q_number < len(self.q_list)

    def next_question(self):
        answer = input(
            f"Q.{self.q_number+1}: {self.q_list[self.q_number].question} (True or False): ")
        game = self.check_answer(answer)
        self.q_number += 1

    def check_answer(self, answer):
        if self.q_list[self.q_number].answer == answer:
            print("You got it right!")
            self.score += 1
            game = True
        else:
            print("You got it wrong!")
            game = False
        print(f"The right answer is: {self.q_list[self.q_number].answer}")
        print(f"Your current score is: {self.score}/{self.q_number+1}\n\n")
        return game

    def end_game_msg(self):
        print(
            f"You've completed the quiz!\nYour final score was: {self.score}/{len(self.q_list)}")
