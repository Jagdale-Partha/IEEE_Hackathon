from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')
def register(request):
    return render(request, 'core/register.html')
