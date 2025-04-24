#Certificate/views.py
from datetime import timezone
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import CreateView, DetailView
from si.models import AffectingFactors
from utils.decorators import measurement_type_required
# from diplomtest.utils.decorators import measurement_type_required
from .forms import CertificateForm
from django.shortcuts import render
from django.utils.decorators import method_decorator
from .models import Certificate
from django.contrib.auth import get_user_model
from django.views.generic.edit import FormMixin
from .forms import AffectingFactorsForm
from journals.models import JournalVerification, JournalEnvironment  # Import JournalVerification and JournalEnvironment
from django.shortcuts import get_object_or_404  
from django.views.generic import ListView
from django.http import HttpResponse
from django.template.loader import get_template, render_to_string
from django.utils.dateparse import parse_date
from xhtml2pdf import pisa
from weasyprint import HTML

User = get_user_model()

def generate_cert_number():
    last_num = Certificate.objects.order_by('-id').first()
    return f"ВНИКТИ/{timezone.now().strftime('%d-%m-%Y')}/{last_num.id + 1:09d}"



class CertificateListView(ListView):
    model = Certificate
    template_name = 'certificates/certificate_list.html'  # Шаблон для отображения
    context_object_name = 'certificates'  # Имя переменной в шаблоне

# class CertificateCreateView(CreateView):
#     model = Certificate
#     form_class = CertificateForm
#     template_name = 'certificates/create.html'
#     success_url = '/certificates/{id}/'
# certificates/views.py
class CertificateCreateView(CreateView):
    model = Certificate                                 #######
    form_class = CertificateForm
    template_name = 'certificates/create.html'
    success_url = '/certificates/'                              #######
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['existing_certificates'] = Certificate.objects.all()  # Список всех свидетельств
        if self.request.POST:
            context['affecting_factors_form'] = AffectingFactorsForm(self.request.POST)
        else:
            context['affecting_factors_form'] = AffectingFactorsForm()
        return context
    
    def get_form_kwargs(self):
        """Передаем текущего пользователя в форму"""
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def form_valid(self, form):
        """Автоматическое заполнение поверителя"""
        context = self.get_context_data()
        affecting_factors_form = context['affecting_factors_form']
        if affecting_factors_form.is_valid():
            affecting_factors = affecting_factors_form.save()
            form.instance.affecting_factors = affecting_factors
            return super().form_valid(form)
        else:
            return self.form_invalid(form)
    
    def test_func(self):
        """Проверка наличия прав у пользователя"""
        return (
            self.request.user.is_authenticated and 
            hasattr(self.request.user, 'employee') and
            self.request.user.employee.measurement_types.exists()
        )


class CertificateDetailView(DetailView):
    model = Certificate
    template_name = 'certificates/detail.html'


def home(request):
    return render(request, 'certificates/home.html')  # Укажите ваш шаблон

# certificates/views.py
def some_view(request):
    employee = request.user.employee
    allowed_types = employee.measurement_types.all()

# from django.views.generic import CreateView, DetailView
# from .models import Certificate

# class CertificateCreateView(CreateView):
#     model = Certificate
#     fields = '__all__'
#     template_name = 'certificates/create.html'

# class CertificateDetailView(DetailView):
#     model = Certificate
#     template_name = 'certificates/detail.html'

# certificates/views.py
@method_decorator(measurement_type_required('Теплофизические измерения'), name='dispatch')
class TemperatureCertificateCreateView(CertificateCreateView):
    template_name = 'certificates/temperature_create.html'

class CertificateCreateFromExampleView(CreateView):
    model = Certificate
    form_class = CertificateForm
    template_name = 'certificates/create.html'
    success_url = '/certificates/'

    def get_initial(self):
        example_certificate = get_object_or_404(Certificate, pk=self.kwargs['pk'])
        initial = super().get_initial()
        # Копируем данные из выбранного свидетельства
        initial.update({
            'verification_date': example_certificate.verification_date,
            'next_verification_date': example_certificate.next_verification_date,
            'si': example_certificate.si,
            'verification_type': example_certificate.verification_type,
            'verification_method': example_certificate.verification_method,
            'verification_result': example_certificate.verification_result,
            'interval': example_certificate.interval,
            'previous_verification_mark': example_certificate.previous_verification_mark,
            'is_vn': example_certificate.is_vn,
            'mark_in_passport': example_certificate.mark_in_passport,
            'mark_on_si': example_certificate.mark_on_si,
            'affecting_factors': example_certificate.affecting_factors,
            'comment': example_certificate.comment,
            'gov_reg_number': example_certificate.gov_reg_number,
            'inventory_number': example_certificate.inventory_number,
            'modification': example_certificate.modification,
            'status': example_certificate.status,
            'organization_name': example_certificate.organization_name,
            'inn': example_certificate.inn,
            'department_head': example_certificate.department_head,
            'verifier': example_certificate.verifier,
            'composition': example_certificate.composition,
        })
        return initial

class CertificatePrintView(DetailView):
    model = Certificate
    template_name = 'certificates/print.html'

    def render_to_pdf(self, template_src, context_dict):
        template = get_template(template_src)
        html = template.render(context_dict)
        response = HttpResponse(content_type='application/pdf')
        pisa_status = pisa.CreatePDF(html, dest=response)
        if pisa_status.err:
            return HttpResponse('Ошибка при создании PDF', status=400)
        return response

    def get(self, request, *args, **kwargs):
        context = {'object': self.get_object()}
        return self.render_to_pdf(self.template_name, context)
    


# def verification_pdf_view(request):
#     start_date = request.GET.get('start_date')
#     end_date = request.GET.get('end_date')

#     entries = JournalVerification.objects.all()
#     if start_date:
#         entries = entries.filter(certificate__verification_date__gte=parse_date(start_date))
#     if end_date:
#         entries = entries.filter(certificate__verification_date__lte=parse_date(end_date))

#     context = {
#         'entries': entries,
#         'start_date': start_date,
#         'end_date': end_date,
#     }

#     html_string = render_to_string('journals/verification_pdf.html', context)
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'inline; filename="journal_verification.pdf"'
#     HTML(string=html_string).write_pdf(response)

#     return response


# def environment_pdf_view(request):
#     start_date = request.GET.get('start_date')
#     end_date = request.GET.get('end_date')

#     entries = JournalEnvironment.objects.all()
#     if start_date:
#         entries = entries.filter(measurement_date__gte=parse_date(start_date))
#     if end_date:
#         entries = entries.filter(measurement_date__lte=parse_date(end_date))

#     context = {
#         'entries': entries,
#         'start_date': start_date,
#         'end_date': end_date,
#     }

#     html_string = render_to_string('journals/environment_pdf.html', context)
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'inline; filename="journal_environment.pdf"'
#     HTML(string=html_string).write_pdf(response)

#     return response