from django.shortcuts import render

from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "commercial/index.html"

class LoginView(TemplateView):
    template_name = "login.html"