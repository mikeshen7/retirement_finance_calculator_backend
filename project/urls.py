from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
# from rest_framework_simplejwt import views as jwt_views
# from .views import MyTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Redirect URL
    path('', lambda req: redirect('admin/')),

    # Endpoints
    path('api/v1/tax_brackets/', include('tax_brackets.urls')),
    path('api/v1/deductions/', include('deductions.urls')),
    path('api/v1/returns/', include('returns.urls')),

    # Login Endpoint
    path('api-auth', include("rest_framework.urls")),

    # JWT URLS
    # path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
