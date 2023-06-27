from django.http import HttpResponse
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from django.forms import ModelForm
from django.urls import reverse_lazy


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['emp_id', 'emp_name', 'emp_email', 'emp_contact']


def index(request):
    return render(request, 'index.html')


# class EmployeeListView(ListView):
#     model = Employee
#
#
# class EmployeeDetailView(DetailView):
#     model = Employee


class EmployeeView(View):
    def get(self, request, *args, **kwargs):
        details = Employee.objects.all()
        return render(request, './templates/employees_list.html', {'details': details})


# class EmployeeUpdateView(UpdateView):
#     model = Employee
#     fields = ['emp_id', 'emp_name', 'emp_email', 'emp_contact']
#     template_name = 'employee_update.html'
#     success_url = reverse_lazy('employee_list')
#
#
# class EmployeeDeleteView(DeleteView):
#     model = Employee
#     success_url = reverse_lazy('employee_list')
