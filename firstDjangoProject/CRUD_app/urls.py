from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('employees/create/', views.EmployeeCreateView.as_view(), name='employee_create'),
    path('employees/', views.EmployeeListView.as_view(), name='employee_list'),
    path('view/<int:pk>', views.EmployeeDetailView.as_view(), name='employee_view'),
    path('update/<int:pk>', views.EmployeeUpdateView.as_view(), name='employee_update'),
    path('delete/<int:pk>', views.EmployeeDeleteView.as_view(), name='employee_delete'),
]
