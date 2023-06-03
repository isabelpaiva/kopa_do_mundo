class NegativeTitlesError(Exception):
    def __init__(self, message, status):
        self.message = message,
        self.status = int(status)

class InvalidYearCupError(Exception):
    def __init__(self, message, status):
        self.message = message,
        self.status = int(status)

class ImpossibleTitlesError(Exception):
    def __init__(self, message, status):
        self.message = message,
        self.status = int(status)
