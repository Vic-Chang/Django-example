from django.shortcuts import render


# home 的 Controller
def home(request):
    return render(request, 'home/home.html')
