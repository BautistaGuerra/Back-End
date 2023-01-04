from django.http import HttpResponse, HttpResponseNotFound


def handler404(request, exception):
    return HttpResponseNotFound('404 Error: Page not found!')
