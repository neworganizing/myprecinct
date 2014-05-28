from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

class SplashView(TemplateView):
    
    template_name = 'splash.html'

    def get(self, request, **kwargs):

        context = self.get_context_data()

        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):

        context = {}

        return context


class HomeView(TemplateView):

    template_name = 'index.html'

    def get(self, request, **kwargs):

        context = self.get_context_data()

        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):

        context = {}

        return context