from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html', {})


def services(request):
    return render(request, 'services.html', {})


def home(request):
    return render(request, 'index.html', {})


def graphics(request):
    return render(request, 'graphics.html', {})


def commercial_adverts(request):
    return render(request, 'commercial_adverts.html', {})


def documentaries(request):
    return render(request, 'documentaries.html', {})


def photography(request):
    return render(request, 'photography.html', {})


def internet_solutions(request):
    return render(request, 'internet_solutions.html', {})


def data_processing(request):
    return render(request, 'data_processing.html', {})