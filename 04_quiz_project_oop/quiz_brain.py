class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        print(f"Q.{self.question_number + 1}: {current_question.text}: ")
        for option in current_question.options:
            print(option)
        user_answer = input("Choose the correct option (a,b,c,d): ")
        self.check_answer(user_answer,current_question.answer)
        self.question_number += 1

    def check_answer(self,user_answer,correct_option):
        if user_answer.lower() == correct_option.lower():
            self.score +=  1
            print("You got it right!!!")
        else:
            print("Thats wrong.")
        print(f"The correct answer was:{correct_option}.")  
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")