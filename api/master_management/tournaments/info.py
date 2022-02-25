from django.views import View
from .models import *


class TournamentInfo(View):
    @staticmethod
    def list_data(instance):
        result = {}
        if instance:
            result["id"] = instance.id
            result["tournament_name"] = instance.tournament_name
            result["total_players"]=instance.total_players
        return result

    @staticmethod
    def details_data(instance):
        result = {}
        if instance:
            result["id"] = instance.id
            result["tournament_name"] = instance.tournament_name
            result["season"] = instance.season.season
            result["tournament_type"] = instance.tournament_type
            result["total_players"] = instance.total_players
            result["winner"] = instance.winner.name
            result["runners_up"] = instance.runners_up.name
            result["second_runners_up"] = instance.second_runners_up.name
            result["top_Goal_Scorer"] = instance.top_Goal_Scorer.name
            result["start_date"] = instance.start_date
            result["end_date"] = instance.end_date
            
        return result



    
   
    
   
