from django.shortcuts import render

# Create your views here.
def name(request):
    return render(request, 'accounts/name.html')

def gender(request):
    return render(request, 'accounts/gender.html')

def birth(request):
    return render(request, 'accounts/birth.html')

def alarm(request):
    return render(request, 'accounts/alarm.html')

def setting(request):
    return render(request, 'accounts/setting.html')