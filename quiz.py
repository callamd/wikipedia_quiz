from app.utils import get_random_infobox
from app.utils import make_question
from app.utils import victor_thing


while True:
    page = get_random_infobox()

    q, a = make_question(page)

    if not q or if not a:
        continue

    user_answer = input(q + "?")
    if user_answer == a:
        print("Congratulations, you're correct!")
        continue
    else:
        print("You stupid or something bruh?")
