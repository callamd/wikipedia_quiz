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
            topic = r.url.split("/")[-1]
            page = wptools.page(topic, silent=True)
            paragraph = page.get("wikitext")
            break
        except Exception as e:
            continue

    return paragraph.data["exrest"]
