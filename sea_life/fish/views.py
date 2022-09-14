# adoption/views.py
from django.http import HttpResponse


def index(req):
    return HttpResponse("<h1>Hello! Here are all the fish!<h1>")


def show(req, id):
    return HttpResponse(f'<h3>Fish number {id}!</h3>')


def about(req):
    return HttpResponse(f'<h3>About some Fish !</h3>')
