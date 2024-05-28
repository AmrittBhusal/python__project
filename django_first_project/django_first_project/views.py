from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("HELLO,word.welcome in Django home page")
    return render(request,'website/index.html')
def about(request):
    return HttpResponse("HELLO,word.welcome in Django about page")
def contact(request):
    return HttpResponse("HELLO,word.welcome in Django contact page")
