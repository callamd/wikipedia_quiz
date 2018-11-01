import re
from Levenshtein.StringMatcher import StringMatcher
from Levenshtein import ratio

paragraph = "Singur Reservoir is a reservoir formed by back waters of Singur Dam located on Manjira River in Medak District, Telangana, India. It is a sustained drinking water source of Hyderabad city.[1][2]"
class Question(object):

    def __init__(self, paragraph):
        self.reg = re.compile(r"([a-zA-Z ]+) (is a| was a) ([a-zA-Z -]+)")
        self.match = self.reg.match(paragraph)
        self.groups = None
        self.answer = None
        if self.match:
            self.groups = self.match.groups()
            self.subject = self.groups[0]
            self.answer = self.groups[2] # May have more than 3

    def is_valid(self):
        return self.groups is not None

    def question(self):
        return "What is {}".format(self.subject)

    def is_correct(self, provided_answer):
        self.levenshtein = StringMatcher(self.answer, provided_answer)
        distance = self.levenshtein.distance()
        good_distance = len(self.answer)
        #print(ratio(self.answer.lower(), provided_answer.lower()))
        return ratio(self.answer.lower(), provided_answer.lower()) > 0.4
