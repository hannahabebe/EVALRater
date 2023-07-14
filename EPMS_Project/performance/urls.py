from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("menu", views.menu, name="menu"),
    path('panel/dashboard', views.dashboard, name='dashboard'),
    path('panel/department', views.department, name='department'),
    path('panel/employee', views.employee, name='employee'),
    path('panel/training', views.training, name='training'),
    path('panel/development', views.development, name='development'),
    # path('panel/order', views.order, name='order'),
    # path('panel/file', views.file, name='file'),
]