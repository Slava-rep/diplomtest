from django.shortcuts import render
from .models import SI  # Убедитесь, что модель SI определена в models.py
from django.views.generic import ListView  # Добавьте этот импорт

from django.db.models import Q  # Добавляем недостающий импорт
from .models import SI  # Импорт модели SI
from django.views.generic import TemplateView


# si/views.py
from django.http import JsonResponse
class SIListView(ListView):
    model = SI
    template_name = 'si/si_list.html'  # Укажите правильный путь к шаблону
    context_object_name = 'si_list'

    # def get_queryset(self):
    #     # Жестко задаем типы средств измерений, которые нужно отобразить
    #     return SI.objects.filter(type__name__in=['Тип 1', 'Тип 2', 'Тип 3'])

# Класс для отображения статичных данных
class StaticSIListView(TemplateView):
    template_name = 'si/si_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Статичные данные для таблицы
        context['si_list'] = [
            {
                'type': 'Датчики давления, преобразователи давления',
                'measurement_range': '(-10 – 1600) кПа',
                'accuracy': 'ПГ ± (0,35 - 1) %',
                'notes': '',
                'additional_notes': ''
            },
            {
                'type': 'Измерители температурные',
                'measurement_range': '(0 – 150) °C, (0 – 800) °C',
                'accuracy': 'ПГ ± 1 %',
                'notes': '',
                'additional_notes': ''
            },
            {
                'type': 'Амперметры и вольтметры, миллиамперметры, милливольтметры щитовые',
                'measurement_range': '(0 – 10) А, (0 – 1000) В',
                'accuracy': 'КТ 0,2',
                'notes': '',
                'additional_notes': ''
            },
            {
                'type': 'Преобразователи напряжения постоянного тока ПН1',
                'measurement_range': '(0 – 1500) В',
                'accuracy': 'ПГ ± 1 %',
                'notes': '',
                'additional_notes': ''
            },
        ]
        return context

def si_autocomplete(request):
    query = request.GET.get('query', '')
    results = SI.objects.filter(
        Q(registration_number__icontains=query) |
        Q(type__name__icontains=query)
    ).values('id', 'registration_number', 'type__name')[:10]
    return JsonResponse(list(results), safe=False)

