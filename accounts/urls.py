from django.urls import path
from .views import landing_page_view, login_view, logout_view, dashboard_view

urlpatterns = [
    path('landing_page/', landing_page_view, name='landing_page'),
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
   path('dashboard/', dashboard_view, name='dashboard'),
    # outras rotas do seu aplicativo aqui
]