from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('employees/create/', views.employee_create, name='employee_create'),
    path('employees/', views.employee_list, name='employee_list'),
    path('view/<int:pk>', views.employee_view, name='employee_view'),
    path('update/<int:pk>', views.employee_update, name='employee_update'),
    path('delete/<int:pk>', views.employee_delete, name='employee_delete'),
]
