from django.urls import path

from . import views


app_name='lists'

urlpatterns = [
    path('',views.home_page,name='index'),
    path('listview/',views.list_view,name='listview')
]


