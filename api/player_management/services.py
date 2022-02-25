from django.db.models import Q
from api.common.repos.services import FetchServices, SaveServices
from .info import *


class PlayerServices(View):
    @staticmethod
    def fetch_profiles(data):
        # Fetching pagination information
        page_size = data.get("page_size")
        page_number = data.get("page")

        # Making Filter queries
        filter_query = PlayerServices.add_filter_queries(data)
        # Adding Search Queries
        filter_query = PlayerServices.add_search_queries(
            data,
            filter_query
        )
        # Making Order Queries
        order_query = PlayerServices.add_order_queries(data)
        # Fetching related instances
        instances = FetchServices.all_instances(
            "api",
            "Player",
            filter_query=filter_query,
            order_query=order_query,
            page_size=page_size,
            page_number=page_number
        )
        # Making response output
        result = [PlayerInfo.list_data(instance) for instance in instances]
        return result

    @staticmethod
    def fetchProfileById(instance_id):
        instance = FetchServices.instance_by_id(
            "api",
            "Player",
            instance_id,
        )
        result = PlayerInfo.details_data(instance)
        return result

    @staticmethod
    def save(data):
        columns = {
            'name' : data.get("name"),
            'pes_id' : data.get("pes_id"),
            'whats_app' : data.get("whats_app"),
            'team_photo' : data.get("team_photo")
        }
        
        instance = SaveServices.save_instance(
            "api",
            "Player",
            columns
        )
        return instance

    @staticmethod
    def update(instance_id, data):
        columns = {
            'name' : data.get("name"),
            'pes_id' : data.get("pes_id"),
            'whats_app' : data.get("whats_app"),
            'team_photo' : data.get("team_photo")
        }

        filter_query = Q(
            id=instance_id
        )

        instance = SaveServices.update_instance(
            "api",
            "Player",
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
            "Player",
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
