from django.shortcuts import render

# Create your views here.
def loading(request):
    return render(request, 'diaries/loading.html')

def info(request):
    return render(request, 'diaries/info.html')

def index(request):
    return render(request, 'diaries/index.html')