from django.urls import path
from . import views

from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('athkar/<int:athkar_id>/', views.athkar_detail, name='athkar_detail'),
    path('athkar_massa/', views.athkar_massa, name='athkar_massa'),
    path('athkar_sabah/', views.athkar_sabah, name='athkar_sabah'),
]
