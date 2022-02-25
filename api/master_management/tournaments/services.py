from django.db.models import Q
from api.common.repos.services import FetchServices, SaveServices
from .info import *


class TournamentServices(View):
    @staticmethod
    def fetch_profiles(data):
        # Fetching pagination information
        page_size = data.get("page_size")
        page_number = data.get("page")

        # Making Filter queries
        filter_query = TournamentServices.add_filter_queries(data)
        # Adding Search Queries
        filter_query = TournamentServices.add_search_queries(
            data,
            filter_query
        )
        # Making Order Queries
        order_query = TournamentServices.add_order_queries(data)
        # Fetching related instances
        instances = FetchServices.all_instances(
            "api",
            "Tournament",
            filter_query=filter_query,
            order_query=order_query,
            page_size=page_size,
            page_number=page_number
        )
        # Making response output
        result = [TournamentInfo.list_data(instance) for instance in instances]
        return result

    @staticmethod
    def fetchProfileById(instance_id):
        instance = FetchServices.instance_by_id(
            "api",
            "Tournament",
            instance_id,
        )
        result = TournamentInfo.details_data(instance)
        return result

    @staticmethod
    def save(data):
        columns = {
           'tournament_name' : data.get("tournament_name"),
           'season' : data.get("season"),
           'tournament_type' : data.get("tournament_type"),
           'total_players' : data.get("total_players"),
           'winner' : data.get("winner"),
           'runners_up' : data.get("runners_up"),
           'second_runners_up' : data.get("second_runners_up"),
           'top_Goal_Scorer' : data.get("top_Goal_Scorer"),
           'start_date' : data.get("start_date"),
           'end_date' : data.get("end_date"),
        }
        
        instance = SaveServices.save_instance(
            "api",
            "Tournament",
            columns
        )
        return instance

    @staticmethod
    def update(instance_id, data):
        columns = {
           'tournament_name' : data.get("tournament_name"),
           'season' : data.get("season"),
           'tournament_type' : data.get("tournament_type"),
           'total_players' : data.get("total_players"),
           'winner' : data.get("winner"),
           'runners_up' : data.get("runners_up"),
           'second_runners_up' : data.get("second_runners_up"),
           'top_Goal_Scorer' : data.get("top_Goal_Scorer"),
           'start_date' : data.get("start_date"),
           'end_date' : data.get("end_date"),
        }

        filter_query = Q(
            id=instance_id
        )

        instance = SaveServices.update_instance(
            "api",
            "Tournament",
            filter_query,
            columns,
        )

        return instance

    @staticmethod
    def delete(instance_id):
        filter_query = Q(
            id=instance_id
        )

        SaveServices.delete_instances(
            "api",
            "Tournament",
            filter_query
        )

        return True

    @staticmethod
    def add_filter_queries(data):
        filter_query = Q()
        return filter_query

    @staticmethod
    def add_search_queries(data, filter_query):
        search = data.get("search")
        if search:
            filter_query.add(
                Q(name__icontains=search),
                Q.AND
            )
        return filter_query

    @staticmethod
    def add_order_queries(data):
        order_query = ["id"]
        return order_query
