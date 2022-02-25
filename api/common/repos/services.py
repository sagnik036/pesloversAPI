from django.apps import apps
from django.views import View
from api.common.paginator.pagination import paginated_data


class FindTables(View):
    @staticmethod
    def get_table(app_name, table_name):
        table = apps.get_model(
            app_label=app_name,
            model_name=table_name
        )
        return table


class FetchServices(View):
    @staticmethod
    def all_instances(app_name, table_name, filter_query=None, order_query=None, page_size=None, page_number=None):
        # Fetch table by app name and table name
        table = FindTables.get_table(
            app_name,
            table_name
        )

        # Filters Data if filter query passed else returns all
        if filter_query:
            filter_data = table.objects.filter(filter_query)
        else:
            filter_data = table.objects.all()

        # Ordering if order query passed, else by default ordered by ID
        if order_query:
            filter_data = filter_data.order_by(*order_query)
        else:
            filter_data = filter_data.order_by("id")

        # Paginate if pagination passed else return all instances
        if page_size and page_number:
            # Pagination
            instances = paginated_data(
                page_size,
                page_number,
                filter_data
            )
        else:
            instances = filter_data
        return instances

    @staticmethod
    def first_instance(app_name, table_name, filter_query=None):
        instances = FetchServices.all_instances(
            app_name,
            table_name,
            filter_query
        )
        instance = instances.order_by(
            "id"
        ).first()
        return instance

    @staticmethod
    def last_instance(app_name, table_name, filter_query=None):
        instances = FetchServices.all_instances(
            app_name,
            table_name,
            filter_query
        )
        instance = instances.order_by(
            "-id"
        ).first()
        return instance

    @staticmethod
    def instance_by_id(app_name, table_name, _id):
        # Fetch table by app name and table name
        table = FindTables.get_table(
            app_name,
            table_name
        )
        try:
            instance = table.objects.get(
                id=_id
            )
        except table.DoesNotExist:
            instance = None
        return instance

    @staticmethod
    def total_objects(app_name, table_name, filter_query=None):
        result = FetchServices.all_instances(
            app_name,
            table_name,
            filter_query
        ).count()
        return result


class SaveServices(View):
    @staticmethod
    def save_instance(app_name, table_name, columns):
        table = FindTables.get_table(
            app_name,
            table_name
        )
        instance = table.objects.create(
            **columns
        )
        return instance

    @staticmethod
    def update_instance(app_name, table_name, filter_query, columns):
        table = FindTables.get_table(
            app_name,
            table_name
        )
        table.objects.filter(
            filter_query
        ).update(
            **columns
        )
        return True

    @staticmethod
    def delete_instances(app_name, table_name, filter_query):
        table = FindTables.get_table(
            app_name,
            table_name
        )
        table.objects.filter(
            filter_query
        ).delete()
        return True
