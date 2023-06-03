from exceptions import ImpossibleTitlesError, InvalidYearCupError, NegativeTitlesError


def data_processing(**data):
    first_cup = int(data["first_cup"].split("-")[0])
    try:
        if data["titles"] < 0:
            raise NegativeTitlesError({"error": "titles cannot be negative"}, 400)
         
    except NegativeTitlesError as error:
        print(error.message)
    try: 
        if first_cup < 1930:
            raise InvalidYearCupError({"error": "there was no world cup this year"}, 400)
        if (first_cup - 1930) % 4 != 0:
            raise InvalidYearCupError({"error": "there was no world cup this year"}, 400)
    except InvalidYearCupError as error:
        print(error.message)
    try: 
        if first_cup >= 2022:
            raise ImpossibleTitlesError( {"error": "impossible to have more titles than disputed cups"}, 400)
    except InvalidYearCupError as error:
        print(error.message)