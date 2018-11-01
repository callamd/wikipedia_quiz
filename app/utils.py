import wptools
import requests

def get_random_paragrah():
    """
    Retard
    Returns paragraph of text for parsing.
    """

    r = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    page = r.url
    print(page)
    topic = r.url.split("/")[-1]
    page = wptools.page(topic)
    paragraph = page.get("wikitext")

    return paragraph.data["exrest"]

