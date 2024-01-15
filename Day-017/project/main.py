from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []
for question in question_data:
    q_text = question["text"]
    q_answer = question["answer"]
    new_question = Question(question_text=q_text, answer_text=q_answer)
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("Congratulations, you completed the quiz!")
print(f"Your final score was {quiz_brain.score} out of {quiz_brain.question_number}.")
