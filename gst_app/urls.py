from django.urls import path
from . import views

urlpatterns = [
    path('', views.department_list, name='department_list'),
    path('department/<int:id>/', views.department_detail, name='department_detail'),
    path('item/', views.item_page, name='item_page'),
    path('unauthorized/', views.unauthorized, name='unauthorized'),
    path('approve_request/<int:request_id>/', views.approve_request, name='approve_request'),
    path('decline_request/<int:request_id>/', views.decline_request, name='decline_request'),
    path('trust/', views.trust_dashboard, name='trust_dashboard'),

]
