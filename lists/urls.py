from django.urls import path

from . import views


app_name='lists'

urlpatterns = [
    path('',views.home_page,name='index'),
    path('ali/',views.home_number2,name='home_number2')
]


