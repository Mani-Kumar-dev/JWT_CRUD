from django.urls import path
from .views import get_trees, create_tree, update_tree, delete_tree, calculate_oxygen_production
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    
    path('api/trees/', get_trees, name='get_trees'),
    path('api/trees/create/', create_tree, name='create_tree'),
    path('api/trees/update/<int:pk>/', update_tree, name='update_tree'),
    path('api/trees/delete/<int:pk>/', delete_tree, name='delete_tree'),
    path('api/trees/calculate_oxygen/', calculate_oxygen_production, name='calculate_oxygen'),
]
