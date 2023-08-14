from django.urls import path
from dashboard.views import *
urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    # outras rotas do seu aplicativo aqui
]