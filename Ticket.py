import datetime


class Ticket:
    # TODO: What else do we want an entry to contain?
    def __init__(self, previous_owner, owner, price):
        self.time = datetime.datetime.now()
        self.tid = None
        self.prev_owner = previous_owner   # This should be an object,
        self.owner = owner
        self.price = price
        self.resale_count = 0

    def __repr__(self):
        if self.prev_owner == "source":
            return "Ticket {} is owned by {}. Created at {}.\n".format(
                self.tid, self.owner, self.time)
        else:
            return "Ticket {} is owned by {}. Bought for ${} at {} from {}.\n".format(
                self.tid, self.owner, self.price, self.time, self.prev_owner)

    def hashable(self):
        return str(self.time) + str(self.tid) \
               + str(self.prev_owner) + str(self.owner) \
               + str(self.price) + str(self.resale_count)
