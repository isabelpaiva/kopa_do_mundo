from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms.models import model_to_dict
from .models import Team


class TeamView(APIView):
    def post(self, request):
        team_new = request.data
        first_cup = int(team_new["first_cup"].split("-")[0])
        if team_new["titles"] < 0:
            return Response({"error": "titles cannot be negative"}, 400)
        if first_cup < 1930:
            return Response({"error": "there was no world cup this year"}, 400)
        if (first_cup - 1930) % 4 != 0:
            return Response({"error": "there was no world cup this year"}, 400)
        if first_cup >= 2022:
            return Response(
                {"error": "impossible to have more titles than disputed cups"}, 400
            )
        new_team = Team.objects.create(**team_new)
        return Response(model_to_dict(new_team), 201)

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
