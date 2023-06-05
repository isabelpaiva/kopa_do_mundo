from django.forms import model_to_dict
from rest_framework.views import APIView
from rest_framework.response import Response
from exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError
from teams.models import Team


class TeamView(APIView):
    def get(self, request):
        all_teams = Team.objects.values()
        return Response(all_teams)
    
    def post(self, request):
        team_new = request.data
        first_cup = int(team_new["first_cup"].split("-")[0])

        try:
            if team_new["titles"] < 0:
                raise NegativeTitlesError()
            
            if first_cup < 1930:
                raise InvalidYearCupError()
            
            if (first_cup - 1930) % 4 != 0:
                raise InvalidYearCupError()

            if first_cup >= 2022:
                raise ImpossibleTitlesError()

            new_team = Team.objects.create(**team_new)
            return Response(model_to_dict(new_team), 201)

        except NegativeTitlesError as e:
            return Response({"error": e.message}, 400)

        except InvalidYearCupError as e:
            return Response({"error": e.message}, 400)

        except ImpossibleTitlesError as e:
            return Response({"error": e.message}, 400)



class TeamDetailView(APIView):
    def get(self, request, team_id):
        try:
            unique_team = Team.objects.get(id=team_id)
            return Response(model_to_dict(unique_team), 200)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)

