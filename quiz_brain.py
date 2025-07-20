class QuizBrain:
    def __init__(self,question_list):
        self.ques_no = 0
        self.ques_list = question_list
        self.score = 0
    def still_has_questions(self):
        if self.ques_no == 12:
            return False
        return True
    def next_question(self):
        current_question = self.ques_list[self.ques_no]
        self.ques_no += 1
        print(f"Q.{self.ques_no }: {current_question.text} ")
    def check_answer(self):
        user_choice = input("True/False")
        current_question = self.ques_list[self.ques_no]
        correct_answer = current_question.answer

        if user_choice == correct_answer:
            self.score += 1
            print("You got it right!")
        else:
            print("Wrong answer!")
        print(f"The correct answer was : {correct_answer}")
        print(f"Your score is: {self.score}/{self.ques_no}" )
