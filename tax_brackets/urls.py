from django.urls import path
from .views import TaxBracketList, TaxBracketDetail

urlpatterns = [
    path('', TaxBracketList.as_view(), name='tax_bracket_list'),
    path('<int:pk>', TaxBracketDetail.as_view(), name='tax_bracket_detail'),
]
