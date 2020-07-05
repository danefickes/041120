from Question import Question

question_prompt = ["My name is? \n(a) Jim\n(b) Dane\n\n",
                   "I like? \n(a) apples\n(b) mangos "]

questions = [
    Question(question_prompt[0], "b"),
    Question(question_prompt[1], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(f"You got {score} out of {len(questions)}")

run_test(questions)