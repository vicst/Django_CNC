from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, DetailView
import random
from .models import form

# Create your views here.
# def home(request):
#     return render(request, "home.html", {"con_var" : "o variabila context"})
#
# def formular1(request):
#     return render(request, "formular1.html", {"con_var" : "o variabila context"})
#
# def formular2(request):
#     return render(request, "formular2.html", {"con_var" : "o variabila context"})
#
# def instructiuni(request):
#     return render(request, "instructiuni.html", {"con_var" : "o variabila context"})

# class ContactView(View):
#     def get(self, request, *args, **kwargs):
#         context = {}
#         return render(request, "contact.html", context)

class HomeView(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        num = random.randint(0,100)
        centralizator = form.objects.all()
        context = {"lista_date" : centralizator}
        return context

class Formular1View(TemplateView):
    template_name = "formular1.html"

class FormularDetailView(DetailView):
    model = form
    template_name = "detail.html"
    def get_context_data(self,**kwargs):
        print (self.kwargs)
        context = super().get_context_data(**kwargs)
        print (context)
        return context



#
# class Formular2View(TemplateView):
#     template_name = "formular2.html"
#
# class InstructiuniView(TemplateView):
#     template_name = "instructiuni.html"
#
# class ContactView(TemplateView):
#     template_name = "contact.html"






