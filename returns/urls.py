from django.urls import path
from .views import ReturnList, ReturnDetail

urlpatterns = [
    path('', ReturnList.as_view(), name='return_list'),
    path('<int:pk>', ReturnDetail.as_view(), name='return_detail'),
]
