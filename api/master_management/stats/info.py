from django.views import View
from .models import *


class Stats_Info(View):
    @staticmethod
    def list_data(instance):
        result = {}
        if instance:
            result["id"] = instance.id
            result["player_name"] = instance.player_name.name
            result["tournament_name"] = instance.tournament.tournament_name
            result["goals"]=instance.goals
        return result

    # @staticmethod
    # def details_data(instance):
    #     result = {}
    #     if instance:
    #         result["id"] = instance.id
    #         result["season"] = instance.season_id
    #         result["tournament_type"] = instance.tournament_type
    #         result["total_players"] = instance.total_players
    #         result["winner"] = instance.winner_id
    #         result["runners_up"] = instance.runners_up_id
    #         result["second_runners_up"] = instance.second_runners_up_id
    #         result["top_Goal_Scorer"] = instance.top_Goal_Scorer_id
    #         result["start_date"] = instance.start_date
    #         result["end_date"] = instance.end_date
            
    #     return result



    
   
    
   
