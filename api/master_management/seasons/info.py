from django.views import View
from .models import *


class SeasonInfo(View):
    @staticmethod
    def list_data(instance):
        result = {}
        if instance:
            result["id"] = instance.id
            result["season"] = instance.season
            result["active_status"]=instance.is_active
        return result



    
   
    
   
