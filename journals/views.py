from django.shortcuts import render
from django.views.generic import ListView
from .models import JournalRegistration, JournalVerification, JournalEnvironment
from django.views.generic import TemplateView
from django.utils.dateparse import parse_date
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import JournalRegistration
from django.utils.dateparse import parse_date
import os
from django.conf import settings
from django.contrib.staticfiles import finders
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import logging
from xhtml2pdf import pisa
from weasyprint import HTML
from django.template.loader import render_to_string

pisa.showLogging()  
logging.basicConfig(level=logging.DEBUG)

# Найдем абсолютный путь к файлу шрифта из статики
font_path = finders.find('fonts/DejaVuSans.ttf')
if not font_path or not os.path.exists(font_path):
    raise IOError("Не найден файл шрифта DejaVuSans.ttf в static/fonts")
# Регистрируем шрифт в ReportLab
pdfmetrics.registerFont(TTFont('DejaVuSans', font_path))
# (Опционально) если используете семейство bold/italic, добавьте их тоже






class JournalRegistrationListView(ListView):
    model = JournalRegistration
    template_name = 'journals/registration_list.html'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        if start_date:
            queryset = queryset.filter(receipt_date__gte=parse_date(start_date))
        if end_date:
            queryset = queryset.filter(receipt_date__lte=parse_date(end_date))
        return queryset
    
class JournalVerificationListView(ListView):
    model = JournalVerification
    template_name = 'journals/verification_list.html'
    
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
    
    
class JournalEnvironmentListView(ListView):
    model = JournalEnvironment
    template_name = 'journals/environment_list.html'
    context_object_name = "environment_journals"

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
class JournalHubView(TemplateView):
    template_name = 'journals.html' #template_name = 'journals/hub.html'

def link_callback(uri, rel):
    # оставляем, чтобы картинки/другие стили работали
    if uri.startswith(settings.STATIC_URL):
        path = uri.replace(settings.STATIC_URL, '')
    else:
        path = uri
    result = finders.find(path)
    if result:
        return result
    abs_path = os.path.join(settings.BASE_DIR, path)
    if os.path.exists(abs_path):
        return abs_path
    return uri

# def generate_pdf(template_src, context_dict, filename):
#     html = get_template(template_src).render(context_dict)

#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = f'attachment; filename=\"{filename}\"'

#     # Обратите внимание: добавляем encoding='UTF-8'
#     pisa_status = pisa.CreatePDF(
#         src=html,
#         dest=response,
#         link_callback=link_callback,
#         encoding='UTF-8'          # ← это критично :contentReference[oaicite:1]{index=1}
#     )

#     if pisa_status.err:
#         return HttpResponse('Ошибка при создании PDF', status=400)
#     return response


# def registration_pdf_view(request):
#     start_date = request.GET.get('start_date')
#     end_date   = request.GET.get('end_date')

#     entries = JournalRegistration.objects.all()
#     if start_date:
#         entries = entries.filter(receipt_date__gte=parse_date(start_date))
#     if end_date:
#         entries = entries.filter(receipt_date__lte=parse_date(end_date))

#     context = {
#         'entries': entries,
#         'start_date': start_date,
#         'end_date': end_date,
#     }
#     return generate_pdf(
#         template_src='journals/registration_pdf.html',
#         context_dict=context,
#         filename='journal_registration.pdf'
#     )


def registration_pdf_view(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    entries = JournalRegistration.objects.all()
    if start_date:
        entries = entries.filter(receipt_date__gte=parse_date(start_date))
    if end_date:
        entries = entries.filter(receipt_date__lte=parse_date(end_date))

    context = {
        'entries': entries,
        'start_date': start_date,
        'end_date': end_date,
    }

    # Рендерим HTML в строку
    html_string = render_to_string('journals/registration_pdf.html', context)

    # Генерируем PDF с помощью WeasyPrint
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="journal_registration.pdf"'
    HTML(string=html_string).write_pdf(response)

    return response

def verification_pdf_view(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    entries = JournalVerification.objects.all()
    if start_date:
        entries = entries.filter(certificate__verification_date__gte=parse_date(start_date))
    if end_date:
        entries = entries.filter(certificate__verification_date__lte=parse_date(end_date))

    context = {
        'entries': entries,
        'start_date': start_date,
        'end_date': end_date,
    }

    html_string = render_to_string('journals/verification_pdf.html', context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="journal_verification.pdf"'
    HTML(string=html_string).write_pdf(response)

    return response


def environment_pdf_view(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    entries = JournalEnvironment.objects.all()
    if start_date:
        entries = entries.filter(measurement_date__gte=parse_date(start_date))
    if end_date:
        entries = entries.filter(measurement_date__lte=parse_date(end_date))

    context = {
        'entries': entries,
        'start_date': start_date,
        'end_date': end_date,
    }

    html_string = render_to_string('journals/environment_pdf.html', context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="journal_environment.pdf"'
    HTML(string=html_string).write_pdf(response)

    return response





















# def generate_pdf(template_src, context_dict):
#     template = get_template(template_src)
#     html = template.render(context_dict)
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="journal_registration.pdf"'
#     pisa_status = pisa.CreatePDF(html, dest=response)
#     if pisa_status.err:
#         return HttpResponse('Ошибка при создании PDF', status=400)
#     return response

# def registration_pdf_view(request):
#     start_date = request.GET.get('start_date')
#     end_date = request.GET.get('end_date')
#     queryset = JournalRegistration.objects.all()
#     if start_date:
#         queryset = queryset.filter(receipt_date__gte=parse_date(start_date))
#     if end_date:
#         queryset = queryset.filter(receipt_date__lte=parse_date(end_date))
#     context = {
#         'entries': queryset,
#         'start_date': start_date,
#         'end_date': end_date,
#     }
#     return generate_pdf('journals/registration_pdf.html', context)