from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Return
from .serializer import ReturnSerializer
from django.db.models import Q
# from rest_framework.response import Response


class ReturnList(ListCreateAPIView):
    queryset = Return.objects.all()
    serializer_class = ReturnSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        # Search queries
        search_query_year = self.request.query_params.getlist('year', None)
        search_query_asset_class = self.request.query_params.getlist(
            'asset_class', None)

        # Filter by year
        if search_query_year:
            queryset = queryset.filter(year__in=search_query_year)

        # Filter by asset class (case-insensitive)
        if search_query_asset_class:
            asset_class_query = Q()
            for asset_class in search_query_asset_class:
                asset_class_query |= Q(asset_class__icontains=asset_class)
            queryset = queryset.filter(asset_class_query)

        return queryset


class ReturnDetail(RetrieveUpdateDestroyAPIView):
    queryset = Return.objects.all()
    serializer_class = ReturnSerializer
