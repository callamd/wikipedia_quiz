import wptools
import requests

def get_random_infobox():
    """
    Callam

    Returns infobox data in k, v format (dict)
    """

    r = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    page = r.url
    print(page)
    topic = r.url.split("/")[-1]
    page = wptools.page(topic)
    paragraph = page.get("wikitext")

    return paragraph.data["exrest"]

print(get_random_infobox())

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
