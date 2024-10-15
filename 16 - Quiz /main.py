from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

#Creates an empty list
question_bank = []

#Iterates every question in question_data
for question in question_data:
    #Creates a new object 'question_to_add'
    question_to_add = Question(question["text"], question["answer"])
    #Appends the object to the list
    question_bank.append(question_to_add)

#Creates a new object of class QuizBrain
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("You've completed the quiz!")
print(f"Final score: {quiz.score}/{quiz.question_number}\n")
