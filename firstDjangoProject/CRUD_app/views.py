from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from django.forms import ModelForm


class EmployeeForm(ModelForm):  # used to define a form for updating or creating Employee Object
    class Meta:
        model = Employee
        fields = ['emp_id', 'emp_name', 'emp_email', 'emp_contact']


def index(request):   # retrieve form page
    return render(request, 'index.html')


def employee_list(request):
    details = Employee.objects.all()
    return render(request, 'employee_list.html', {'details': details})


def employee_view(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employee_view.html', {'employee': employee})


def employee_create(request):
    if request.method == "POST":
        emp_id = request.POST['emp_id']
        emp_name = request.POST['emp_name']
        emp_email = request.POST['emp_email']
        emp_contact = request.POST['emp_contact']
        obj = Employee.objects.create(emp_id=emp_id, emp_name=emp_name, emp_email=emp_email, emp_contact=emp_contact)
        obj.save()
        return redirect('employee_list')


def employee_delete(request, pk):
    Employee.objects.filter(id=pk).delete()
    return redirect('employee_list')


def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, 'employee_update.html', {'form': form})

