from django.contrib import admin
from django.urls import path, include
from gst_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('hod/', views.hod_dashboard, name='hod_dashboard'),
    path('principal/', views.principal_dashboard, name='principal_dashboard'),
    path('trust/', views.trust_dashboard, name='trust_dashboard'),
    path('logout/', views.logout_view, name='logout'),
]
