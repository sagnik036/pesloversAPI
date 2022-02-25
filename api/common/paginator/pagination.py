from django.core.paginator import (Paginator, cached_property)


class TimeLimitedPaginator(Paginator):
    @cached_property
    def count(self):
        return 9999999999


def paginated_data(limit=10, page=1, data=None):
    # ============== setup for pagination ================
    if data is None:
        data = []
    record_size = int(limit)
    # ============== end setup for pagination ============

    paginator = TimeLimitedPaginator
    paginator = paginator(data, int(record_size))
    result = paginator.get_page(page)

    if result:
        try:
            result = result
        except Exception as e:
            print(e)
            result = paginated_data.object_list
    return result
