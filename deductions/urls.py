from django.urls import path
from .views import DeductionList, DeductionDetail

urlpatterns = [
    path('', DeductionList.as_view(), name='deduction_list'),
    path('<int:pk>', DeductionDetail.as_view(), name='deduction_detail'),
]
