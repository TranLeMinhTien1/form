from django import views
from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm, sendEmail
from django.views import View
# Create your views here.

class indexClass(View):
    def get(self, request):
        return HttpResponse("hello")

def add_post(request):
    a = PostForm()
    return render(request, 'news/add_news.html', {'f':a})

class ClassSaveNews(View):
    def get(self, request):
        a = PostForm()
        return render(request, 'news/add_news.html', {'f':a})
    def post(self, request):
        g = PostForm(request.POST)
        if g.is_valid(): #Khớp dữ liệu không
            g.save()
            return HttpResponse("Lưu OK")
        else:
            return HttpResponse("Không save dc")
    
def email_view(request):
    b = sendEmail()
    return render(request, 'news/email.html', {'f':b})

def process(request):
    if request.method == "POST":
        m = sendEmail(request.POST)
        if m.is_valid():
            tieude=m.cleaned_data['title']
            cc = m.cleaned_data['cc']
            noidung = m.cleaned_data['content']
            Email = m.cleaned_data['email']
            context= {'td':tieude, 'c':cc, 'b': noidung, 'd':Email}
            return render(request, 'news/print_email.html', context)
        else:
            return HttpResponse('Form not validate')
    else:
        return HttpResponse('Erro')

