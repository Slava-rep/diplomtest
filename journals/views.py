from django.shortcuts import render
from django.views.generic import ListView, View
from django.http import HttpResponse
from django.template.loader import render_to_string, get_template
from django.utils.dateparse import parse_date
from weasyprint import HTML
from xhtml2pdf import pisa
from .models import JournalsJournalregistration, JournalsJournalverification, JournalsJournalenvironment
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

@login_required
def hub(request):
    return render(request, 'journals/hub.html')

class JournalRegistrationListView(LoginRequiredMixin, ListView):
    model = JournalsJournalregistration
    template_name = 'journals/registration_list.html'
    context_object_name = 'object_list'
    login_url = '/login/'  # URL для перенаправления неавторизованных пользователей

    def get_queryset(self):
        queryset = super().get_queryset()
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        if start_date:
            queryset = queryset.filter(receipt_date__gte=parse_date(start_date))
        if end_date:
            queryset = queryset.filter(receipt_date__lte=parse_date(end_date))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['start_date'] = self.request.GET.get('start_date', '')
        context['end_date'] = self.request.GET.get('end_date', '')
        return context

class JournalVerificationListView(LoginRequiredMixin, ListView):
    model = JournalsJournalverification
    template_name = 'journals/verification_list.html'
    context_object_name = 'object_list'
    login_url = '/login/'

    def get_queryset(self):
        queryset = super().get_queryset()
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        if start_date:
            queryset = queryset.filter(certificate__verification_date__gte=parse_date(start_date))
        if end_date:
            queryset = queryset.filter(certificate__verification_date__lte=parse_date(end_date))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['start_date'] = self.request.GET.get('start_date', '')
        context['end_date'] = self.request.GET.get('end_date', '')
        return context

class JournalEnvironmentListView(LoginRequiredMixin, ListView):
    model = JournalsJournalenvironment
    template_name = 'journals/environment_list.html'
    context_object_name = 'object_list'
    login_url = '/login/'

    def get_queryset(self):
        queryset = super().get_queryset()
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        if start_date:
            queryset = queryset.filter(measurement_date__gte=parse_date(start_date))
        if end_date:
            queryset = queryset.filter(measurement_date__lte=parse_date(end_date))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['start_date'] = self.request.GET.get('start_date', '')
        context['end_date'] = self.request.GET.get('end_date', '')
        return context

@login_required
def registration_pdf_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
        
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    entries = JournalsJournalregistration.objects.all()
    if start_date:
        entries = entries.filter(receipt_date__gte=parse_date(start_date))
    if end_date:
        entries = entries.filter(receipt_date__lte=parse_date(end_date))

    context = {
        'entries': entries,
        'start_date': parse_date(start_date) if start_date else None,
        'end_date': parse_date(end_date) if end_date else None,
    }

    html_string = render_to_string('journals/registration_pdf.html', context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="journal_registration.pdf"'
    
    HTML(string=html_string).write_pdf(response, presentational_hints=True)
    return response

@login_required
def verification_pdf_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
        
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    entries = JournalsJournalverification.objects.all()
    if start_date:
        entries = entries.filter(certificate__verification_date__gte=parse_date(start_date))
    if end_date:
        entries = entries.filter(certificate__verification_date__lte=parse_date(end_date))

    context = {
        'entries': entries,
        'start_date': parse_date(start_date) if start_date else None,
        'end_date': parse_date(end_date) if end_date else None,
    }

    html_string = render_to_string('journals/verification_pdf.html', context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="journal_verification.pdf"'
    
    HTML(string=html_string).write_pdf(response, presentational_hints=True)
    return response

@login_required
def environment_pdf_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
        
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    entries = JournalsJournalenvironment.objects.all()
    if start_date:
        entries = entries.filter(measurement_date__gte=parse_date(start_date))
    if end_date:
        entries = entries.filter(measurement_date__lte=parse_date(end_date))

    context = {
        'entries': entries,
        'start_date': parse_date(start_date) if start_date else None,
        'end_date': parse_date(end_date) if end_date else None,
    }

    html_string = render_to_string('journals/environment_pdf.html', context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="journal_environment.pdf"'
    
    HTML(string=html_string).write_pdf(response, presentational_hints=True)
    return response