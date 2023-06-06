from exceptions import ImpossibleTitlesError, InvalidYearCupError, NegativeTitlesError
from datetime import date

def data_processing(data: dict):
    first_cup = int(data["first_cup"].split("-")[0])
    today = date.today()
    first_cup = data["first_cup"]
    first_cup = int(first_cup[0:4])
    year_verify = today.year - first_cup

    if data["titles"] < 0:
        raise NegativeTitlesError()

    if first_cup < 1930 or (first_cup - 1930) % 4 != 0:
        raise InvalidYearCupError()
    
    if (year_verify/4) < data["titles"]:
        raise ImpossibleTitlesError()