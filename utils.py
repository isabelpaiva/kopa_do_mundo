from exceptions import ImpossibleTitlesError, InvalidYearCupError, NegativeTitlesError

def data_processing(data):
    first_cup = int(data["first_cup"].split("-")[0])

    if data["titles"] < 0:
        raise NegativeTitlesError("titles cannot be negative")

    if first_cup < 1930 or (first_cup - 1930) % 4 != 0:
        raise InvalidYearCupError("there was no world cup this year")
    
    if first_cup <= 2022:
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")

