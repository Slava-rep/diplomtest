# employees/views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Employee, EmployeeMeasurementType
from .forms import EmployeeForm

class EmployeeListView(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'employees/employee_list.html'
    context_object_name = 'employees'
    
    def get_queryset(self):
        # Фильтрация для не-админов
        if not self.request.user.is_superuser:
            return Employee.objects.filter(user=self.request.user)
        return super().get_queryset()

class EmployeeCreateView(UserPassesTestMixin, CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employees/employee_form.html'
    success_url = reverse_lazy('employees:list')
    
    def test_func(self):
        # Только админы могут создавать сотрудников
        return self.request.user.is_superuser
    
    def form_valid(self, form):
        # Привязка к текущему пользователю-администратору
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class EmployeeUpdateView(UserPassesTestMixin, UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employees/employee_form.html'
    success_url = reverse_lazy('employees:list')
    
    def test_func(self):
        # Админы или сам сотрудник могут редактировать
        return self.request.user.is_superuser or self.get_object().user == self.request.user

class EmployeeDeleteView(UserPassesTestMixin, DeleteView):
    model = Employee
    template_name = 'employees/employee_confirm_delete.html'
    success_url = reverse_lazy('employees:list')
    
    def test_func(self):
        # Только админы могут удалять
        return self.request.user.is_superuser

class EmployeeDetailView(LoginRequiredMixin, DetailView):
    model = Employee
    template_name = 'employees/employee_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем связанные виды измерений
        context['measurement_types'] = self.object.measurement_types.all()
        return context

# Дополнительные функции для работы с видами измерений
class EmployeeMeasurementUpdateView(UserPassesTestMixin, UpdateView):
    model = EmployeeMeasurementType
    fields = ['measurement_type']
    template_name = 'employees/measurement_type_form.html'
    
    def test_func(self):
        return self.request.user.is_superuser
    
    def get_success_url(self):
        return reverse_lazy('employees:detail', kwargs={'pk': self.object.employee.pk})