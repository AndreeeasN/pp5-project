from django.shortcuts import render


def handler404(request, exception):
    """
    Handles errorcode 404 - page not found
    """
    return render(request, "errors/404.html", status=404)
