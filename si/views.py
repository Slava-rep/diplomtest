from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import SiVerificationtype, SiVerificationmethod, SiAffectingfactors, SiReference
from .forms import (
    SiVerificationmethodForm, SiAffectingfactorsForm, SiReferenceForm
)
from django.utils.decorators import method_decorator

class SiHomeView(LoginRequiredMixin, TemplateView):
    template_name = 'si/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['verification_types'] = SiVerificationtype.objects.all()
        context['verification_methods'] = SiVerificationmethod.objects.all()
        context['affecting_factors'] = SiAffectingfactors.objects.all()
        context['references'] = SiReference.objects.all()
        return context

@method_decorator(login_required, name='dispatch')
class SiVerificationtypeListView(LoginRequiredMixin, ListView):
    model = SiVerificationtype
    template_name = 'si/verificationtype_list.html'
    context_object_name = 'verification_types'

@method_decorator(login_required, name='dispatch')
class SiVerificationmethodListView(LoginRequiredMixin, ListView):
    model = SiVerificationmethod
    template_name = 'si/verificationmethod_list.html'
    context_object_name = 'verification_methods'

@method_decorator(login_required, name='dispatch')
class SiVerificationmethodCreateView(LoginRequiredMixin, CreateView):
    model = SiVerificationmethod
    form_class = SiVerificationmethodForm
    template_name = 'si/verificationmethod_form.html'
    success_url = reverse_lazy('si:verificationmethod_list')

@method_decorator(login_required, name='dispatch')
class SiVerificationmethodUpdateView(LoginRequiredMixin, UpdateView):
    model = SiVerificationmethod
    form_class = SiVerificationmethodForm
    template_name = 'si/verificationmethod_form.html'
    success_url = reverse_lazy('si:verificationmethod_list')

@method_decorator(login_required, name='dispatch')
class SiVerificationmethodDeleteView(LoginRequiredMixin, DeleteView):
    model = SiVerificationmethod
    template_name = 'si/verificationmethod_confirm_delete.html'
    success_url = reverse_lazy('si:verificationmethod_list')

@method_decorator(login_required, name='dispatch')
class SiAffectingfactorsListView(LoginRequiredMixin, ListView):
    model = SiAffectingfactors
    template_name = 'si/affectingfactors_list.html'
    context_object_name = 'affecting_factors'

@method_decorator(login_required, name='dispatch')
class SiAffectingfactorsCreateView(LoginRequiredMixin, CreateView):
    model = SiAffectingfactors
    form_class = SiAffectingfactorsForm
    template_name = 'si/affectingfactors_form.html'
    success_url = reverse_lazy('si:affectingfactors_list')

@method_decorator(login_required, name='dispatch')
class SiAffectingfactorsUpdateView(LoginRequiredMixin, UpdateView):
    model = SiAffectingfactors
    form_class = SiAffectingfactorsForm
    template_name = 'si/affectingfactors_form.html'
    success_url = reverse_lazy('si:affectingfactors_list')

@method_decorator(login_required, name='dispatch')
class SiAffectingfactorsDeleteView(LoginRequiredMixin, DeleteView):
    model = SiAffectingfactors
    template_name = 'si/affectingfactors_confirm_delete.html'
    success_url = reverse_lazy('si:affectingfactors_list')

@method_decorator(login_required, name='dispatch')
class SiReferenceListView(LoginRequiredMixin, ListView):
    model = SiReference
    template_name = 'si/reference_list.html'
    context_object_name = 'references'

    def get_queryset(self):
        return SiReference.objects.all().order_by('standard_type', 'brand')

@method_decorator(login_required, name='dispatch')
class SiReferenceCreateView(LoginRequiredMixin, CreateView):
    model = SiReference
    form_class = SiReferenceForm
    template_name = 'si/reference_form.html'
    success_url = reverse_lazy('si:reference_list')

@method_decorator(login_required, name='dispatch')
class SiReferenceUpdateView(LoginRequiredMixin, UpdateView):
    model = SiReference
    form_class = SiReferenceForm
    template_name = 'si/reference_form.html'
    success_url = reverse_lazy('si:reference_list')

@method_decorator(login_required, name='dispatch')
class SiReferenceDeleteView(LoginRequiredMixin, DeleteView):
    model = SiReference
    template_name = 'si/reference_confirm_delete.html'
    success_url = reverse_lazy('si:reference_list')

def get_verification_methods(request):
    methods = SiVerificationmethod.objects.all()
    data = [{'id': method.id_verification_method, 'name': method.name} for method in methods]
    return JsonResponse(data, safe=False)