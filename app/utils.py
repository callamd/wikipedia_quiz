import wptools
import requests

def get_random_paragraph():
    """
    Callam
    Returns paragraph of text for parsing.
    """
    while True:
        try:
            r = requests.get("https://en.wikipedia.org/wiki/Special:Random")
            page = r.url
            print(page)
            topic = r.url.split("/")[-1]
            page = wptools.page(topic)
            paragraph = page.get("wikitext")
            break
        except Exception as e:
            continue

    return paragraph.data["exrest"]

def make_question():
    """
    Anton

    Create a question.
    """

    return question, answer

def victor_thing():
    """
    Victor

    Whatever you like (ascii dicks?)
    """

    return _, _
