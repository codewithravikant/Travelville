from django.urls import path, include
from .views import hello_pages, get_city_info

urlpatterns = [
    path('', hello_pages),
    path('detail/', get_city_info, name='city_detail')
]
