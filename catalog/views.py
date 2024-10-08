from django.shortcuts import render
def index(request):
    return render(request, 'Hello,Welcome to the page')

