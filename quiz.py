from question_manager import Question
from app.utils import get_random_paragraph
import random

insult_list = [
    "Are you a blithering moron?",
    "Did you actually attend school?",
    "Your IQ is definitely below 50?",
]

def play():
    score = 0
    for i in range(10):
        valid = False
        while not valid:
            paragraph = get_random_paragraph()
            question = Question(paragraph)
            valid = question.is_valid()

        print(question.question() + "?")
        user_answer = input()
        if question.is_correct(user_answer):
            print("Congratulations, you're correct!")
            score += 1
            continue
        else:
            print("{} The answer is: {}".format(random.choice(insult_list), question.answer))
            score += 0
            continue

    print("You got {} out of 10")

    if score< 5:
        print("Idiot..")
    elif score > 5 and score < 8:
        print("Average")
    else:
        print("Genius!")



if __name__ == "__main__":
    print("Welcome to the IQ TEST 1.0")
    play()
