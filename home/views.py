from django.shortcuts import render

def index(request):
    """
    View that displays the index page
    """
    return render(request, 'home/index.html')
