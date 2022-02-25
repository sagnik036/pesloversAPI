from django.views import View
from .models import *


class PlayerInfo(View):
    @staticmethod
    def list_data(instance):
        result = {}
        if instance:
            result["id"] = instance.id
            result["user_code"] = instance.user_code
            result["name"]=instance.name
        return result

    @staticmethod
    def details_data(instance):
        result = {}
        if instance:
            result["id"] = instance.id
            result["user_code"] = instance.user_code
            result["name"]=instance.name
            result["whats_app"]=instance.whats_app
            result["pes_id"]=instance.pes_id
            result["team_photo"]=instance.team_photo
        return result



    
   
    
   
