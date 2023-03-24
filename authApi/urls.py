from django.urls import include, path
from authApi import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[
    path('',views.UserViewSet.as_view({'get': 'list'}) ),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('create/', views.UserCreate.as_view()),
    path('update/<int:pk>/', views.UserUpdate.as_view({'put': 'update'})),
    path('delete/<int:pk>/', views.UserDelete.as_view({'delete': 'destroy'})),
    path('health/', views.HealthCheck.as_view()),
    path('login/', views.Login.as_view()),

]

