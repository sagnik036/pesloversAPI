from django.db.models import Q
from api.common.repos.services import FetchServices, SaveServices
from .info import *


class SeasonServices(View):
    @staticmethod
    def fetch_profiles(data):
        # Fetching pagination information
        page_size = data.get("page_size")
        page_number = data.get("page")

        # Making Filter queries
        filter_query = SeasonServices.add_filter_queries(data)
        # Adding Search Queries
        filter_query = SeasonServices.add_search_queries(
            data,
            filter_query
        )
        # Making Order Queries
        order_query = SeasonServices.add_order_queries(data)
        # Fetching related instances
        instances = FetchServices.all_instances(
            "api",
            "Season",
            filter_query=filter_query,
            order_query=order_query,
            page_size=page_size,
            page_number=page_number
        )
        # Making response output
        result = [SeasonInfo.list_data(instance) for instance in instances]
        return result

    @staticmethod
    def fetchProfileById(instance_id):
        instance = FetchServices.instance_by_id(
            "api",
            "Season",
            instance_id,
        )
        result = SeasonInfo.list_data(instance)
        return result

    @staticmethod
    def save(data):
        columns = {
            'season' : data.get("season"),
            'is_active' : data.get("is_active"),
        }
        
        instance = SaveServices.save_instance(
            "api",
            "Season",
            columns
        )
        return instance

    @staticmethod
    def update(instance_id, data):
        columns = {
           'season' : data.get("season"),
           'is_active' : data.get("is_active"),
        }

        filter_query = Q(
            user_code=instance_id
        )

        instance = SaveServices.update_instance(
            "api",
            "Season",
            filter_query,
            columns,
        )

        return instance

    @staticmethod
    def delete(instance_id):
        filter_query = Q(
            user_code=instance_id
        )

        SaveServices.delete_instances(
            "api",
            "Season",
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
                Q(season__icontains=search),
                Q.AND
            )
        return filter_query

    @staticmethod
    def add_order_queries(data):
        order_query = ["id"]
        return order_query
