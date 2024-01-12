class Date:

    def __init__(self, month, year):
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.month} {self.year}"


class EndDate:

    def __init__(self, month=None, year=None, present=False):
        self.month = month
        self.year = year
        self.present = present

    def __str__(self):
        if self.present:
            return "Present"
        else:
            return f"{self.month} {self.year}" if self.month and self.year else ""
