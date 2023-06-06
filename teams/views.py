from django.forms import model_to_dict
from rest_framework.views import APIView
from rest_framework.response import Response
from exceptions import ImpossibleTitlesError, InvalidYearCupError, NegativeTitlesError
from teams.models import Team
from utils import data_processing


class TeamView(APIView):

    def post(self, request):
        team_new = request.data
        try:
            data_processing(team_new)
        except (NegativeTitlesError, ImpossibleTitlesError, InvalidYearCupError) as error:
            return Response({"error": error.message}, 400)

        try:
            new_team = Team.objects.create(**team_new)
            return Response(model_to_dict(new_team), 201)
        except Exception as e:
            return Response({"error": str(e)}, 400)
    
    def get(self, request):
        all_teams = Team.objects.values()
        return Response(all_teams)
    
    
class TeamDetailView(APIView):
    def get(self, request, team_id):
        try:
            unique_team = Team.objects.get(id=team_id)
            return Response(model_to_dict(unique_team), 200)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)

    def patch(self, request, team_id):
        try:
            data = request.data.items()
            team = Team.objects.get(id=team_id)
            for key, value in data:
                setattr(team, key, value)
            team.save()
            return Response(model_to_dict(team), 200)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)

    def delete(self, request, team_id):
        try:
            team = Team.objects.get(id=team_id)
            team.delete()
            return Response(status=204)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)
