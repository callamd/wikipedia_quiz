from app.utils import get_random_infobox
from app.utils import make_question
from app.utils import victor_thing

score = 0
while for i in range(10):
    page = get_random_infobox()

    q, a = make_question(page)

    if not q or if not a:
        continue

    user_answer = input(q + "?")
    if user_answer == a:
        print("Congratulations, you're correct!")
        score += 1
        continue
    else:
        print("You stupid or something bruh?")
        score += 0
        continue

    if i >= 10:
        break
print("You got {} out of 10")

if score< 5:
    print("Idiot..")
elif score > 5 and score < 8:
    print("Average")
else:
    print("Genius!")
