from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import CustomTokenObtainPairView, UserDetailView, RegisterView
from django.urls import path
from .views import RealEstatePropertyListView, RealEstatePropertyDetailView, CreateInterestMapView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', UserDetailView.as_view(), name='user_detail'),
    path('properties/', RealEstatePropertyListView.as_view(), name='property-list'),
    path('properties/<uuid:pk>/', RealEstatePropertyDetailView.as_view(), name='property-detail'),
    path('interest-map/', CreateInterestMapView.as_view(), name='interest-map'),
]

