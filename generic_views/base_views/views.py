from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import NamesModel
from .forms import Names
from django.views.generic import TemplateView

# Create your views here.
class ViewForm(View):
    model = Names
    def get(self,request):
        form = self.model()
        return render(request,'base_views/add.html',{'form':form})
    def post(self,request):
        form = self.model(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base_views:index')
        return render(request,'base_views/add.html',{'form':form})

class DeleteView(View):   
    def get(self,request):
        names = NamesModel.objects.all()
        return render(request,'base_views/delete.html',{'names':names})

class ReadView(View):   
    def get(self,request):
        names = NamesModel.objects.all()
        return render(request,'base_views/read.html',{'names':names})

class DeleteRecordView(View):
    def get(self,request,id):
        name = get_object_or_404(NamesModel,id=id)
        name.delete()
        return redirect('base_views:base')

class TemplateOne(TemplateView):
    template_name = "base_views/template_views/template1.html"
    template_number = "1"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['names'] = NamesModel.objects.all()
        context['number'] = self.template_number
        return context


class TemplateTwo(TemplateOne):
    template_name = "base_views/template_views/template2.html"

class TemplateThree(TemplateOne):
    template_name = "base_views/template_views/template3.html"

class TemplateFour(TemplateOne):
    template_number = "40"
    template_name = "base_views/template_views/template4.html"



