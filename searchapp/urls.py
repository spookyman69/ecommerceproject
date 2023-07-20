from django.urls import path
from . import views

app_name='searchapp'
urlpatterns=[
    path('search_details',views.search_result,name="search_result")
]