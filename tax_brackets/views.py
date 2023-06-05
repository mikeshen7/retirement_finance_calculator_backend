from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Tax_Bracket
from .serializer import TaxBracketSerializer
from django.db.models import Q
# from rest_framework.response import Response


class TaxBracketList(ListCreateAPIView):
    queryset = Tax_Bracket.objects.all()
    serializer_class = TaxBracketSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        # Search queries
        search_query_year = self.request.query_params.getlist('year', None)
        search_query_filing_status = self.request.query_params.getlist(
            'filing_status', None)
        search_query_tax_type = self.request.query_params.getlist(
            'tax_type', None)

        # Filter by year
        if search_query_year:
            queryset = queryset.filter(year__in=search_query_year)

        # Filter by filing status
        if search_query_filing_status:
            queryset = queryset.filter(
                filing_status__in=search_query_filing_status)

        # Filter by tax type status
        if search_query_filing_status:
            queryset = queryset.filter(tax_type__in=search_query_tax_type)

        return queryset


class TaxBracketDetail(RetrieveUpdateDestroyAPIView):
    queryset = Tax_Bracket.objects.all()
    serializer_class = TaxBracketSerializer
