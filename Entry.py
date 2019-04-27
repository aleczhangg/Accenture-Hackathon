import datetime


class Entry:
    # TODO: What else do we want an entry to contain?
    def __init__(self, person):
        self.datetime = datetime.datetime.now()
        self.date = self.datetime.today()
        self.time = self.datetime.strftime("%H:%M:%S")
        self.person = person
        self.message = ""

    def __repr__(self):
        return "{} committed at {}\n".format(self.person, self.time)

    def hashable(self):
        return str(self.time) + str(self.person) + str(self.message)
