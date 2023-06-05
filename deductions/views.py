from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Deduction
from .serializer import DeductionSerializer
from django.db.models import Q
# from rest_framework.response import Response


class DeductionList(ListCreateAPIView):
    queryset = Deduction.objects.all()
    serializer_class = DeductionSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        # Search queries
        search_query_year = self.request.query_params.getlist('year', None)
        search_query_filing_status = self.request.query_params.getlist(
            'filing_status', None)

        # Filter by year
        if search_query_year:
            queryset = queryset.filter(year__in=search_query_year)

        # Filter by filing status
        if search_query_filing_status:
            queryset = queryset.filter(
                filing_status__in=search_query_filing_status)

        return queryset


class DeductionDetail(RetrieveUpdateDestroyAPIView):
    queryset = Deduction.objects.all()
    serializer_class = DeductionSerializer
