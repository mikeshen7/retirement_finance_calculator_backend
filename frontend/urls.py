from django.urls import path
from .views import home, tax_calc_form, tax_calc_output, budget, other_links, LoginView

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('tax_calc_form', tax_calc_form.as_view(), name='tax_calc_form'),
    path('tax_calc_output', tax_calc_output.as_view(), name='tax_calc_output'),
    path('budget', budget.as_view(), name='budget'),
    path('other_links', other_links.as_view(), name='other_links'),
    path('login', LoginView.as_view(), name='login'),

]
