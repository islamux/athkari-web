from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('athkar/<int:athkar_id>/', views.athkar_detail, name='athkar_detail'),
]
