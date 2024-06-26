import keyword
from re import search
from django.db.models import Q
from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank,
    SearchHeadline,
)

from goods.models import Products


def q_search(query):

    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))

    vector = SearchVector("name", "description", "vendorCode")

    query = SearchQuery(query)

    return (
        Products.objects.annotate(rank=SearchRank(vector, query))
        .filter(rank__gt=0)
        .order_by("-rank")
    )

    # result = (
    #     Products.objects.annotate(rank=SearchRank(vector, query))
    #     .filter(rank__gt=0)
    #     .order_by("-rank")
    # )

    # return result
